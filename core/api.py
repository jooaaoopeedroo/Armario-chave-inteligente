# core/api.py
from django.db import connection
from ninja import NinjaAPI, Path, Schema

# Instância principal do Django Ninja
api = NinjaAPI(
    title="API Armário Inteligente SENAI",
    version="1.0.0",
    description="Serviços RESTful para validação e controle de chaves RFID/NFC"
)


# 1. Schemas Pydantic (DTOs de Entrada e Saída)
class StatusResponseSchema(Schema):
    status: str
    servidor: str
    versao: str


class ConsultaUUIDSchema(Schema):
    uuid: str
    tipo_identificado: str  # 'DOCENTE', 'CHAVE' ou 'DESCONHECIDO'
    autorizado: bool
    mensagem: str


# 2. Endpoint de Saúde do Sistema (Health Check)
@api.get("/status", response=StatusResponseSchema, tags=["Sistema"])
def status_sistema(request):
    """Informa que a API está online (health check)."""
    return {
        "status": "ONLINE",
        "servidor": "Django Ninja + Supabase",
        "versao": "1.0.0"
    }


# 3. Endpoint de Consulta Unificada de UUID
@api.get(
    "/consulta-uuid/{uuid}",
    response={200: ConsultaUUIDSchema, 404: ConsultaUUIDSchema},
    tags=["Portaria / Claviculário"],
)
def consultar_uuid(request, uuid: str = Path(..., min_length=8, max_length=8)):
    """
    Consulta um UUID lido pelo leitor RFID/NFC.
    Identifica se pertence a um docente ativo ou a uma chave e verifica autorização.
    """
    uuid_limpo = uuid.strip().upper()

    # Consulta no banco de dados Supabase via cursor
    with connection.cursor() as cursor:

        # 1. Verifica se é um Crachá de Docente
        cursor.execute(
            "SELECT nm_usuario, st_status FROM tb_usuario WHERE UPPER(uuid_cracha) = %s;",
            [uuid_limpo]
        )
        docente = cursor.fetchone()

        if docente:
            nome, ativo = docente
            if ativo:
                return 200, {
                    "uuid": uuid_limpo,
                    "tipo_identificado": "DOCENTE",
                    "autorizado": True,
                    "mensagem": f"Docente {nome} identificado e ativo."
                }
            return 200, {
                "uuid": uuid_limpo,
                "tipo_identificado": "DOCENTE",
                "autorizado": False,
                "mensagem": f"Acesso Negado: Docente {nome} está inativo."
            }

        # 2. Se não for docente, verifica se é uma Tag de Chave
        cursor.execute(
            """
            SELECT tc.id_espaco, te.st_disponivel
            FROM tb_chave tc
            INNER JOIN tb_espaco te ON tc.id_espaco = te.id_espaco
            WHERE UPPER(tc.uuid_chave) = %s;
            """,
            [uuid_limpo]
        )
        chave = cursor.fetchone()

        if chave:
            id_nicho, livre = chave
            status_nicho = "Livre" if livre else "Ocupado"
            return 200, {
                "uuid": uuid_limpo,
                "tipo_identificado": "CHAVE",
                "autorizado": True,
                "mensagem": f"Chave vinculada ao Nicho #{id_nicho} (Status: {status_nicho})."
            }

    # 3. UUID não localizado no banco
    return 404, {
        "uuid": uuid_limpo,
        "tipo_identificado": "DESCONHECIDO",
        "autorizado": False,
        "mensagem": "Cartão/Tag não cadastrado no sistema."
    }
