# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/ /dev 05/02/2018
"""
08 - Reverso do número. Faça uma função que retorne o reverso de um número
inteiro informado. Por exemplo: 127 -> 721.
"""


def reverso_numero(numero):
    return str(numero)[::-1]


def main():
    numero = int(input("Digite um número: "))
    print(f"O reverso do número digitado é {reverso_numero(numero)}")



if __name__ == '__main__':

    main()
