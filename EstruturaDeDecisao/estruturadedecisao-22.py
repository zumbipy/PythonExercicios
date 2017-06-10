# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaDeDecisao
# Para execurta o programa on line entra no link a baixo:
# https://repl.it/I23A/0
"""
22 - Faça um Programa que peça um número inteiro e determine se ele é
par ou impar. Dica: utilize o operador módulo (resto da divisão).
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
numero = int(input("Digete um numero: "))

# ================================================================================
#                           Logica do programa
# ================================================================================
if numero % 2 == 0:
    print("O numero {} e par.".format(numero))
else:
    print("O numero {} e impar.".format(numero))
