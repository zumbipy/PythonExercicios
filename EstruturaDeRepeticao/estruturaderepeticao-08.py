# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaDeRepeticao
"""
8 - Faça um programa que leia 5 números e informe a soma e a média dos números.
"""
# ================================================================================
#                           Variaveis do Programa.
# ================================================================================
soma = 0
numero = 0

# ================================================================================
#                           Logica do Programa.
# ================================================================================
for i in range(5):
    numero = int(input("Digite numero {} de 5: ".format(i + 1)))
    soma += numero

print("A soma dos 5 numeros é {} e a média é {}".format(soma, soma / 5))
