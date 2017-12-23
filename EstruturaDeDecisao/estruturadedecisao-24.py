# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
24 - Faça um Programa que leia 2 números e em seguida pergunte ao usuário
qual operação ele deseja realizar. O resultado da operação deve ser
acompanhado de uma frase que diga se o número é:
a. par ou ímpar;
b. positivo ou negativo;
c. inteiro ou decimal.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
numero_1 = input("Digite um numero: ")
numero_2 = input("Digite outro numero: ")

operacao = input("""Qual operação você deseja realizar?
Digite (A) para Par ou Impar.
Digite (B) para Positivo ou Negativo.
Digite (C) para Inteiro ou Decimal.
Digite a Altenativa que deseja:
""").upper()

# ================================================================================
#                           Logica do programa
# ================================================================================
if operacao == "A":
    if "." in numero_1:
        numero_1 = round(float(numero_1))
    else:
        numero_1 = int(numero_1)
    if "." in numero_2:
        numero_2 = round(float(numero_2))
    else:
        numero_2 = int(numero_2)
    if numero_1 % 2 == 0:
        print("Numero {} e Par".format(numero_1))
    else:
        print("Numero {} e Impar".format(numero_1))
    if numero_2 % 2 == 0:
        print("Numero {} e Par".format(numero_2))
    else:
        print("Numero {} e Impar".format(numero_2))

elif operacao == "B":
    if "." in numero_1:
        numero_1 = float(numero_1)
    else:
        numero_1 = int(numero_1)
    if "." in numero_2:
        numero_2 = float(numero_2)
    else:
        numero_2 = int(numero_2)

    if numero_1 >= 1:
        print("Numero {} é positivo".format(numero_1))
    else:
        print("Numero {} é negativo".format(numero_1))
    if numero_2 >= 1:
        print("Numero {} é positivo".format(numero_2))
    else:
        print("Numero {} é negativo".format(numero_2))

elif operacao == "C":
    if "." in numero_1:
        print("Numero {} e Decimal".format(numero_1))
    else:
        print("Numero {} e Inteiro".format(numero_1))
    if "." in numero_2:
        print("Numero {} e Decimal".format(numero_2))
    else:
        print("Numero {} e Inteiro".format(numero_2))
else:
    print("Valor invalido")
