# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 26/02/2018
"""
01 - Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e
imprima até a n-ésima linha.
"""


def matrix_print(numero):
    for numero in range(1, numero + 1):
        for p in range(numero):
            print(f'{numero}   ', end="")
        print()


numero = int(input("Digite um numero: "))
matrix_print(numero)
