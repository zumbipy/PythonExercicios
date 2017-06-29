# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaLista
"""
02 - Faça um Programa que leia um vetor de 10 números reais e
mostre-os na ordem inversa.
"""
# =============================================================================
#                           Variáveis do programa é Logica.
# =============================================================================
vetor = [i for i in range(1, 11)]

print("Vetor na ordem normal:")
for i in vetor:
    print("{} ".format(i), end="")
print()

vetor.reverse()
print("Vetor na ordem inversa:")
for i in vetor:
    print("{} ".format(i), end="")
print()
