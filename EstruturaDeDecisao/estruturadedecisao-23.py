# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaDeDecisao
# Para execurta o programa on line entra no link a baixo:
# https://repl.it/I238/0
"""
23 - Faça um Programa que peça um número e informe se o número é inteiro ou
decimal.
Dica: utilize uma função de arredondamento.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
numero_digitado = input("Digite um numero: ")

# ================================================================================
#                           Logica do programa
# ================================================================================
if "." in numero_digitado:
    print("Ele e um numero Decimal")
else:
    print("Ele e um numero Inteiro")
