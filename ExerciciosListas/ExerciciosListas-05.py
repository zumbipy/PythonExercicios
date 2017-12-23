# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaLista
"""
05 - Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os três vetores.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
numeros = None
vetor_par = []
vetor_impares = []
vetor_digitados = []

# ================================================================================
#                           Logica do programa
# ================================================================================
for n in range(1, 21):
    numeros = int(input("Digite {}/20 números inteiros: ".format(n)))
    vetor_digitados.append(numeros)
    if numeros % 2 == 0:
        vetor_par.append(numeros)
    else:
        vetor_impares.append(numeros)

print("lista dos números pares: ")
# end="\n" * 2 = pula 2 linhas.
print(vetor_digitados, end="\n" * 2)

print("lista dos números Digitados: ")
# end="\n" * 2 = pula 2 linhas.
print(vetor_par, end="\n" * 2)

print("Lista dos números impares: ")
print(vetor_impares)
