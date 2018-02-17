# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 17/02/2018
"""
49 - Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
"""


def n_termnos(numero):
    lista_termos = []
    a, b, ta, tb = 1, 1, 0, 0
    for n in range(1, (numero + 1)):
        ta, tb = (ta + a), (tb + b)
        lista_termos.append(f"{a}/{b}")
        a, b = (a + 1), (b + 2)
    lista_termos.append(f'{ta}/{tb}')
    return lista_termos


def imprimir(lista):
    saida = "S ="
    for item in lista:
        if item == lista[-1]:
            saida += f' = {item} '
        else:
            saida += f' {item}'
            if item != lista[-2]:
                saida += " +"
    print(saida)


imprimir(n_termnos(5))
