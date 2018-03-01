# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 26/02/2018
"""
04 - Faça um programa com uma função chamada somaImposto.
A função possui dois parâmetros formais: taxaImposto, que é a quantia de
imposto sobre vendas expressa em porcentagem e custo, que é o custo de um
item antes do imposto. A função “altera” o valor de custo para incluir o
imposto sobre vendas.
"""


def somar_imposto(taxa, valor):
    imposto = (taxa / 100) * valor
    soma = valor + imposto
    return soma


print(somar_imposto(10, 100))

numero1 = int(input("Digite um numero: "))
