# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 26/02/2018
"""
02 - Faça um programa, com uma função que necessite de três argumentos,
e que forneça a soma desses três argumentos.
"""


def soma_tres(n1, n2, n3):
    return n1 + n2 + n3


numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))
numero3 = int(input("Digite outro numero: "))

print(soma_tres(numero1, numero2, numero3))
