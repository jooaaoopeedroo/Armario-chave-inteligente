# simulador.py

from core.regras_acesso import validar_permissao_retirada

# Cenário 1 (Pass)
print(validar_permissao_retirada("1045", 14, True))

# Cenário 2 (Fail)
print(validar_permissao_retirada("1045", 2, True))
print(validar_permissao_retirada("1045", 10, False))
print(validar_permissao_retirada("1045", "Doze horas", True))
