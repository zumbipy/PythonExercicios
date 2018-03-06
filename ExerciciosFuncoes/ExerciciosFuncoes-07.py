# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/ /dev 05/02/2018
"""
07 - Faça uma função que informe a quantidade de dígitos de um determinado
número inteiro informado.
"""


def imforma_digito(numero):
    return len(str(numero))


def main():
    numero = int(input("Digite um numer: "))
    print(f"O numero digitado tem {imforma_digito(numero)} digitos")


if __name__ == '__main__':
    main()
