# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
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
