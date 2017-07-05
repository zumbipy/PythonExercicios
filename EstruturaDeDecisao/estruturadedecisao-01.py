# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaDeDecisao
# Para execurta o programa on line entra no link a baixo:
# https://repl.it/I0h0/0
"""
1 - Faça um programa que peça dois números e imprima o maior deles.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
# Entrada de Dados.

numero0 = int(input("Digite um numero: "))
numero1 = int(input("Digiete outro numero: "))

# Comparação dos valores.
if numero0 > numero1:
    print("O numero {} e maior que o {}".format(numero0, numero1))
else:
    print("O numero {} e maior que o {}".format(numero1, numero0))
