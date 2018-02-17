# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 17/02/2018
"""
48 - Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  12376489
  => 98467321
"""


def inverter_numero(numero):
    tnumero = str(numero)
    saida = ''
    for letra in range((len(tnumero) - 1), -1, -1):
        saida += tnumero[letra]
    return int(saida)


numero = int(input("Digite um numero inteiro positivo: "))
if numero > 0:
    print(inverter_numero(numero))
else:
    print("Número digitado não é positovo.")
