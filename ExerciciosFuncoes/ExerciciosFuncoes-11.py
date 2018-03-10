# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/ /dev 10/03/2018
"""
11 - Embaralha palavra. Construa uma função que receba uma string
como parâmetro e devolva outra string com os carateres embaralhados.
Por exemplo: se função receber a palavra python, pode retornar npthyo,
ophtyn ou qualquer outra combinação possível, de forma aleatória.
Padronize em sua função que todos os caracteres serão devolvidos
em caixa alta ou caixa baixa, independentemente de como foram digitados.
"""
from random import shuffle


def embaralha_palavra(palavra):
    lista_palavra = list(palavra)
    shuffle(lista_palavra)
    saida = "".join(lista_palavra)
    return print(saida.lower())


embaralha_palavra("PyNoobCoding")
