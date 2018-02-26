# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 26/02/2018
"""
03 - Faça um programa, com uma função que necessite de um argumento.
A função retorna o valor de caractere ‘P’, se seu argumento for positivo,
e ‘N’, se seu argumento for zero ou negativo.
"""


def positivo_negativo(numero):
    if numero <= 0:
        print("N")
    else:
        print("P")


for numero in range(-10, 10):
    print(f'{numero} = ', end="")
    positivo_negativo(numero)
