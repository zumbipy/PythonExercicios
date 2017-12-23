# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
6 - Faça um Programa que leia três números e mostre o maior deles.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
# Entrada de Dados.
numero0 = int(input("Digite o Primeiro numero: "))
numero1 = int(input("Digite o Segundo numero: "))
numero2 = int(input("Didite o Terceiro numero: "))

# ================================================================================
#                           Logica Do Programa
# ================================================================================
# Comparaçoes pra sabe qual e o maior entre os 3 digitados.
if numero0 <= numero1 <= numero2 >= numero0:
    print("Numero {} e o maior.".format(numero2))

elif numero0 <= numero1 >= numero2 >= numero0:
    print("Numero {} e o maior.".format(numero1))

elif numero0 >= numero1 <= numero2 >= numero0:
    print("Numero {} e o maior.".format(numero2))

elif numero0 <= numero1 >= numero2 <= numero0:
    print("Numero {} e o maior.".format(numero1))

elif numero0 >= numero1 <= numero2 <= numero0:
    print("Numero {} e o maior.".format(numero0))

elif numero0 >= numero1 >= numero2 <= numero0:
    print("Numero {} e o maior.".format(numero0))
