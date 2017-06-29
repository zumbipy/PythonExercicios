# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaLista
"""
07 - Faça um Programa que leia um vetor de 5 números inteiros,
mostre a soma, a multiplicação e os números.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
vetor = [3, 4, 10, 4, 9]
vetor_soma = 0
vetor_mult = 1

# ================================================================================
#                           Logica do programa
# ================================================================================
for num in vetor:
    vetor_soma += num
    vetor_mult *= num
print("Lista dos Numeros:")
print(vetor, end="\n" * 2)

print("Multiplicação de todos os numeros da lista.")
print(vetor_mult, end="\n" * 2)

print("Soma de todos os numeros da lista.")
print(vetor_soma)
