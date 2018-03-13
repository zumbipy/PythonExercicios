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

def valida_quadrado_magico(lista_quadrado_magico):
    soma = sum([lista_quadrado_magico[0], lista_quadrado_magico[1], lista_quadrado_magico[2]])
    index_adicao = 0
    saida = 1
    for valida in range(3):
        posica1 = lista_quadrado_magico[0 + index_adicao]
        posica2 = lista_quadrado_magico[1 + index_adicao]
        posica3 = lista_quadrado_magico[2 + index_adicao]
        if sum([posica1, posica2, posica3]) == soma:
            saida += 1
        index_adicao += 3
    
    index_adicao = 0
    for valida in range(3):
        posica1 = lista_quadrado_magico[0 + index_adicao]
        posica2 = lista_quadrado_magico[3 + index_adicao]
        posica3 = lista_quadrado_magico[6 + index_adicao]
        if sum([posica1, posica2, posica3]) == soma:
            saida += 1
        index_adicao += 1

    if sum([lista_quadrado_magico[0], lista_quadrado_magico[4], lista_quadrado_magico[8]]) == soma:
        saida += 1

    if sum([lista_quadrado_magico[2], lista_quadrado_magico[4], lista_quadrado_magico[5]]) == soma:
        saida += 1

    return saida


lista = [8, 3, 4, 1, 5, 9, 6, 7, 2]


print(valida_quadrado_magico(lista))

