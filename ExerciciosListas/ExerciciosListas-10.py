# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaLista
"""
10 - Faça um Programa que leia dois vetores com 10 elementos cada.
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser
compostos pelos elementos intercalados dos dois outros vetores.
"""
vetor_1 = list(range(1, 11))
vetor_2 = list(range(11, 21))
vetor_3 = []

for i in range(0, 10):
    vetor_3.append(vetor_1[i])
    vetor_3.append(vetor_2[i])

print("lista 1:")
print(vetor_1)
print()
print("lista 2:")
print(vetor_2)
print()
print("lista 3:")
print(vetor_3)
