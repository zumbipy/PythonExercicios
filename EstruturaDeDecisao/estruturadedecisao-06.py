# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaDeDecisao
# Para execurta o programa on line entra no link a baixo:
# https://repl.it/I0ip/0
"""
6 - Faça um Programa que leia três números e mostre o maior deles.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
# Entrada de Dados.
numero0 = int(input("Digite o Primeiro numero: "))
numero1 = int(input("Digite o Segundo numero: "))
numero2 = int(input("Didite o Terceiro numero: "))

# ================================================================================
#                           Logica Do Programa
# ================================================================================
# Comparaçoes pra sabe qual e o maior entre os 3 digitados.
if numero0 <= numero1 <= numero2 >= numero0:
    print("Numero {} e o maior.".format(numero2))

elif numero0 <= numero1 >= numero2 >= numero0:
    print("Numero {} e o maior.".format(numero1))

elif numero0 >= numero1 <= numero2 >= numero0:
    print("Numero {} e o maior.".format(numero2))

elif numero0 <= numero1 >= numero2 <= numero0:
    print("Numero {} e o maior.".format(numero1))

elif numero0 >= numero1 <= numero2 <= numero0:
    print("Numero {} e o maior.".format(numero0))

elif numero0 >= numero1 >= numero2 <= numero0:
    print("Numero {} e o maior.".format(numero0))
