# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
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
