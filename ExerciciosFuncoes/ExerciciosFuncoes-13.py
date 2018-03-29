# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/ /dev 12/03/2018
"""
13 - Quadrado mágico. Um quadrado mágico é aquele dividido em
linhas e colunas, com um número em cada posição e no qual a
soma das linhas, colunas e diagonais é a mesma. Por exemplo,
veja um quadrado mágico de lado 3, com números de 1 a 9:

8  3  4
1  5  9
6  7  2

Elabore uma função que identifica e mostra na tela todos os
quadrados mágicos com as características acima. Dica:
produza todas as combinações possíveis e verifique a soma
quando completar cada quadrado. Usar um vetor de 1 a 9 parece
ser mais simples que usar uma matriz 3x3.
"""
import random


def quadrado_magico():
    return [8, 3, 4, 1, 5, 9, 6, 7, 2]


def valida(lista):
    N_MAGICO = 15
    saida = 0
    a, b, c, d, e, f, g, h, i = lista

    # Valida linhas
    saida += 1 if sum([d, e, f]) == N_MAGICO else 0
    saida += 1 if sum([a, b, c]) == N_MAGICO else 0
    saida += 1 if sum([g, h, i]) == N_MAGICO else 0

    # Validar colunas
    saida += 1 if sum([a, d, g]) == N_MAGICO else 0
    saida += 1 if sum([b, e, h]) == N_MAGICO else 0
    saida += 1 if sum([c, f, i]) == N_MAGICO else 0

    # Validar diagonal
    saida += 1 if sum([a, e, i]) == N_MAGICO else 0
    saida += 1 if sum([c, e, g]) == N_MAGICO else 0

    if saida == 8:
        return True
    else:
        return False


def imprimir(lista):
    print(f"""
{lista[0]} {lista[1]} {lista[2]}
{lista[3]} {lista[4]} {lista[5]}
{lista[6]} {lista[7]} {lista[8]}""")


def remove_repetido(lista_final, lista_normal):
    if lista_normal in lista_final:
        return True
    else:
        return False


lista_final = []
lista_quadrado_magico = [1, 2, 3, 4, 6, 7, 8, 9]

for equivalente in range(1000000):

    random.shuffle(lista_quadrado_magico)
    lista_quadrado_magico.insert(4, 5)

    if not remove_repetido(lista_final, lista_quadrado_magico) and valida(lista_quadrado_magico):
        lista_final.append(lista_quadrado_magico.copy())
    lista_quadrado_magico.remove(5)

for mostra in lista_final:
    imprimir(mostra)
