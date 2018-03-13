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
    nada = lista.copy()
    index = [3, 0, 1, 6, 4, 2, 7, 8, 5]
    lista.clear()
    for p, modifica in enumerate(index):
        lista.insert(p, nada[modifica])


def valida(lista):
    n_magico = 15
    a, b, c, d, e, f, g, h, i = lista

    # Valida linhas
    saida = True if sum([a, b, c]) else False
    saida = True if sum([d, e, f]) else False
    saida = True if sum([g, h, i]) else False

    # Validar colunas
    saida = True if sum([a, d, g]) else False
    saida = True if sum([b, e, h]) else False
    saida = True if sum([c, f, i]) else False

    # Validar diagonal
    saida = True if sum([a, e, i]) else False
    saida = True if sum([c, e, g]) else False

    return saida


def imprimir(lista):
    print(f"""
{lista[0]} {lista[1]} {lista[2]}
{lista[3]} {lista[4]} {lista[5]}
{lista[6]} {lista[7]} {lista[8]}""")


def ab(lista, p):
    if p in lista:
        return True
    else:
        return False


lista = []
a = quadrado_magico()

for equivalente in range(100):
    gira_frente(a)
    if not ab(lista, a):
        lista.append(a.copy())
    
for mostra in lista:
    imprimir(mostra)
