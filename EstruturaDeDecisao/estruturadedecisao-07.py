# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaDeDecisao
# Para execurta o programa on line entra no link a baixo:
# https://repl.it/I0jJ/1
"""
7 - Faça um Programa que leia três números e mostre o menor deles.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
# Entrada de Dados.
numero0 = int(input("Digite o Primeiro número: "))
numero1 = int(input("Digite o Segundo número: "))
numero2 = int(input("Didite o Terceiro número: "))

# ================================================================================
#                           Logica Do Programa
# ================================================================================
# Comparaçoes pra sabe qual e o menor entre os 3 digitados.
if numero0 <= numero1 <= numero2 >= numero0:
    print("Número {} é o menor.".format(numero0))

elif numero0 <= numero1 >= numero2 >= numero0:
    print("Número {} é o menor.".format(numero0))

elif numero0 >= numero1 <= numero2 >= numero0:
    print("Número {} é o menor.".format(numero1))

elif numero0 <= numero1 >= numero2 <= numero0:
    print("Número {} é o menor.".format(numero2))

elif numero0 >= numero1 <= numero2 <= numero0:
    print("Número {} é o menor.".format(numero1))

elif numero0 >= numero1 >= numero2 <= numero0:
    print("Número {} é o menor.".format(numero2))
