# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a
senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a
pedir as informações.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
# Entrada de Dados.
nome = input("Digite o seu login: ").lower()
senha = input("Digite a senha: ")

# ================================================================================
#                           Lógica do programa
# ================================================================================
# Comparado texto de senha e nome.
while True:
    # comparação de str.
    if senha == nome:
        print("Senha e nome não podem se a mesma.")
        nome = input("!!!Digite o seu login: ")
        senha = input("!!!Digite a senha: ")
    else:
        break
print("Senha e login cadastrado.")
