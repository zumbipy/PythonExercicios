# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 15/02/2018
"""
Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos
restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos
sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média,
conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular
a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de
saída do programa deve ser conforme o exemplo abaixo:
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
"""


def perdir_notas():
    l_notas = []
    for repetir in range(7):
        nota = float(input(f"Digite a nota {repetir + 1}/7: "))
        l_notas.append(nota)
    return l_notas


def media_notas(lista):
    media = lista.copy()
    media.sort()
    return sum(media[1:6]) / 5


def melhor_nota(lista):
    return max(lista)


def pior_nota(lista):
    return min(lista)


def vizualivar_resultado(lista):
    nome, notas, melhor, pior, media = lista

    print(f"Atleta: {nome}")
    for nota in notas:
        print(f"Nota: {nota:.1f}")
    print()
    print(f"""Resultado final:
    Atleta: {nome}
    Melhor nota: {melhor:.1f}
    Pior nota: {pior:.1f}
    Média: {media:.02f}""")


if __name__ == '__main__':
    lista = []
    nome = input("Qual nome do Atlera: ")
    lista.append(nome)

    notas = perdir_notas()
    lista.append(notas)

    lista.append(melhor_nota(notas))
    lista.append(pior_nota(notas))
    lista.append(melhor_nota(notas))

    vizualivar_resultado(lista)
