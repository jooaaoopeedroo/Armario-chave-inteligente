# core/regras_acesso.py

def validar_permissao_retirada(id_cracha: str, horario: int, docente_ativo: bool) -> dict:
    """Verifica as regras de acesso eretornao status."""

    if not docente_ativo:
        return {"autorizado": False, "motivo": "403_INATIVO", "mensagem": "Cadastro Inativo"}

    if horario >= 23 or horario < 5:
        return {"autorizado": False, "motivo": "403_NOTURNO", "mensagem": "Trava Noturna"}

    return {"autorizado": True, "motivo": "200_OK", "mensagem": "Acesso liberado"}
