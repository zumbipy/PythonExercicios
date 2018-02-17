# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 17/02/2018
"""
49 - Faça um programa que mostre os n termos da Série a seguir:
S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
Imprima no final a soma da série.
"""


def n_termnos(numero):
    lista_termos = []
    a, b = 1, 1
    for n in range(1, (numero + 1)):
        lista_termos.append([a, b])
        a, b = (a + 1), (b + 2)
    return lista_termos


def imprimir(lista):
    saida = "S ="
    for item in lista:
        a, b = item
        if item != lista[-1]:
            saida += f' {a}/{b} +'
        else:
            saida += f' {a}/{b}'
        total_item = soma_termos(lista)
    print(f'{saida} = {total_item:.2f}')


def soma_termos(lista):
    return sum([a / b for a, b in lista])


if __name__ == '__main__':
    imprimir(n_termnos(5))
