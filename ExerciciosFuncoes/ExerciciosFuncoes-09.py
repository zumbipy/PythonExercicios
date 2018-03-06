# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/ /dev 05/02/2018
"""
09 -  Jogo de Craps. Faça um programa de implemente um jogo de Craps.
O jogador lança um par de dados, obtendo um valor entre 2 e 12.
Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e
você perdeu.
Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
Seu objetivo agora é continuar jogando os dados até tirar este número
novamente. Você perde, no entanto, se tirar um 7 antes de tirar este
Ponto novamente.
"""
from random import choice


def jogar_dados():
    dado = [2, 3, 4, 5, 6]
    dado1, dado2 = choice(dado), choice(dado)
    return [dado1, dado2]


def validade_resultados(lista):
    soma_numeros = sum(lista)
    if soma_numeros in [7, 11]:
        return True
    if soma_numeros in [2, 3, 12]:
        return False
    if soma_numeros in [4, 5, 6, 8, 9, 10]:
        return None


def main():
    print("Bem vindo ao Jogar Creaps")
    nome = input("Qual seu nome: ")
    print("Jogar dados agora ....")
    while True:

        dados = jogar_dados()
        if validade_resultados(dados):
            print(f"Dado1 {dados[0]} dado2 {dados[1]} total {sum(dados)}")
            print("Você venceu")
            break
        else:
            if validade_resultados(dados) is None:
                print(f"Dado1 {dados[0]} dado2 {dados[1]} total {sum(dados)}")
                print("Jogar de novo")
            else:
                print(f"Dado1 {dados[0]} dado2 {dados[1]} total {sum(dados)}")
                print("Você perdeu.")
                break


if __name__ == '__main__':
    main()