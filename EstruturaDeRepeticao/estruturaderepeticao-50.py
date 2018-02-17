# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 17/02/2018
"""
Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N,
Faça um programa que calcule o valor de H com N termos.
"""


def n_termos(n, h):
    lista_termos = []
    for item in range(2, n + 1):
        lista_termos.append([h, item])
    return lista_termos


def soma_termos(lista):
    total = lista[0][0]
    for a, b in lista:
        total += a / b
    return total


def imprimir(lista):
    saida = f"H = {lista[0][0]}"
    for a, b in lista:
        saida += f" + {a}/{b}"
    print(saida)


if __name__ == '__main__':
    H = 1
    N = 7
    lista = n_termos(N, H)
    imprimir(lista)
    print(f"Total das valor de H com N termos é {soma_termos(lista):.2f}")
