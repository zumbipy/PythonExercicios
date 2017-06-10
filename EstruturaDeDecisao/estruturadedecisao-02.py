# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaDeDecisao
# Para execurta o programa on line entra no link a baixo:
# https://repl.it/I0he/0
"""
2 - Faça um Programa que peça um valor e mostre
na tela se o valor é positivo ou negativo.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
# Entrada de Dados.
valor = int(input("Digite um valor: "))

# Comparação dos valores.
if valor < 0:
    print("Valor {} é negativo".format(valor))
else:
    print("Valor {} é positivo".format(valor))
