# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaLista
"""
11 - Altere o programa anterior, intercalando 3 vetores de
10 elementos cada.
"""
vetor_1 = list(range(1, 11))
vetor_2 = list(range(11, 21))
vetor_3 = list(range(21, 31))
vetor_4 = []

for i in range(0, 10):
    vetor_4.append(vetor_1[i])
    vetor_4.append(vetor_2[i])
    vetor_4.append(vetor_3[i])

print("lista 1:")
print(vetor_1)
print()
print("lista 2:")
print(vetor_2)
print()
print("lista 3:")
print(vetor_3)
print()
print("lista 4:")
print(vetor_4)
