# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/ /dev 10/03/2018
"""
12 - Desenha moldura. Construa uma função que desenhe um retângulo usando os
caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas
e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor
máximo é 20. Se valores fora da faixa forem informados, eles devem ser
modificados para valores dentro da faixa de forma elegante.
"""

def desenhar_moldura(linhas=1, colunas=1):
    if linhas > 20:
        linhas = 1
    if colunas > 20:
        colunas = 5

    print("+"+"--"*colunas+"+")
    for linha in range(linhas):
        print('|'+'  '*colunas+'|')
    print("+" + "--" * colunas + "+")


desenhar_moldura(2,21)