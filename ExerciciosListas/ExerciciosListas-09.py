# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaLista
"""
09 - Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a
soma dos quadrados dos elementos do vetor.
"""

vetor_a = list(range(1, 11))
soma = 0

for i in vetor_a:
    soma += (i ** 2)

print(soma)
