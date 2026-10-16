def rejeitar(motivo):
    """Mostra a mensagem de acesso negado com o motivo."""
    print("Acesso Negado:", motivo)


def bloquear_fechadura():
    """Informa que a fechadura foi bloqueada."""
    print("Fechadura bloqueada")


def liberar_chave():
    """Informa que a chave do Lab 03 foi liberada."""
    print("Chave do Lab 03 Liberada.")


# Dados do docente
docente_requisitante = {
    "nome": "Prof. Silva",
    "ativo": True,
    "id_cracha": 1045,
    "admin": False
}
docente_ativo = docente_requisitante["ativo"]
hora_atual = 14
nicho_ocupado = False

# Funil de decisão
if not docente_ativo:
    rejeitar("Cadastro Inativo")
elif hora_atual >= 23 or hora_atual < 5:
    print("Acesso Negado: Fora do horário comercial.")
    bloquear_fechadura()
    rejeitar("Trava Noturna")
elif nicho_ocupado:
    rejeitar("Chave Indisponível")
else:
    liberar_chave()