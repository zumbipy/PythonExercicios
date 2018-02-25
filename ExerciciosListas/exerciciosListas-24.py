# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 25/02/2018
"""
24 - Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e
armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi
conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros
aleatórios, simulando os lançamentos dos dados.
"""
from random import choice


def jogar_dados():
    return choice([1, 2, 3, 4, 5, 6])


def contar_lados(lista_jogadas):
    resultado = []
    total_lado = 0
    for lado in range(1, 6):
        total_lado = lista_jogadas.count(lado)
        resultado.append([lado, total_lado])
    return resultado


if __name__ == '__main__':
    lista_resultado = []
    for jogadas in range(100):
        lista_resultado.append(jogar_dados())
    total_lados = contar_lados(lista_resultado)

    print("simulando os lançamentos dos dados 100 vezes.")
    print("Resultado foi:")
    for lado, total in total_lados:
        print(f"""lado {lado} = {total} vezes.""")
