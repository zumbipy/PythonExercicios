# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
22 - Faça um Programa que peça um número inteiro e determine se ele é
par ou impar. Dica: utilize o operador módulo (resto da divisão).
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
numero = int(input("Digete um numero: "))

# ================================================================================
#                           Logica do programa
# ================================================================================
if numero % 2 == 0:
    print("O numero {} e par.".format(numero))
else:
    print("O numero {} e impar.".format(numero))
