# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
23 - Faça um Programa que peça um número e informe se o número é inteiro ou
decimal.
Dica: utilize uma função de arredondamento.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
numero_digitado = input("Digite um numero: ")

# ================================================================================
#                           Logica do programa
# ================================================================================
if "." in numero_digitado:
    print("Ele e um numero Decimal")
else:
    print("Ele e um numero Inteiro")
