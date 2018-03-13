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


def quadrado_magico():
    return [8, 3, 4, 1, 5, 9, 6, 7, 2]


def gira_frente(lista):
    index = [3, 0, 1, 6, 4, 2, 7, 8, 5]
    lista = [lista[x] for x in index]
    return lista


def imprimir(lista):
    print(f"""
{lista[0]} {lista[1]} {lista[2]}
{lista[3]} {lista[4]} {lista[5]}
{lista[6]} {lista[7]} {lista[8]}""")


def invert_cima_baixo(lista):
    lista[0], lista[6] = lista[6], lista[0]
    lista[1], lista[7] = lista[7], lista[1]
    lista[2], lista[8] = lista[8], lista[2]


def invert_direita_esqueda(lista):
    lista[2], lista[0] = lista[0], lista[2]
    lista[5], lista[3] = lista[3], lista[5]
    lista[8], lista[6] = lista[6], lista[8]


def valida(lista):
    n_magico = 15
    a, b, c, d, e, f, g, h, i = lista
    if sum([a, b, c]) == n_magico:
        saida = True
    else:
        return False

    if sum([d, e, f]) == n_magico:
        saida = True
    else:
        return False

    if sum([g, h, i]) == n_magico:
        saida = True
    else:
        return False


    if sum([a, d, g]) == n_magico:
        saida = True
    else:
        return False

    if sum([b, e, h]) == n_magico:
        saida = True
    else:
        return False

    if sum([c, f, i]) == n_magico:
        saida = True
    else:
        return False


    if sum([a, e, i]) == n_magico:
        saida = True
    else:
        return False

    if sum([c, e, g]) == n_magico:
        saida = True
    else:
        return False

    return saida


a = quadrado_magico()
if valida(a):
    print("verdade")
imprimir(a)
imprimir(gira_frente(a))