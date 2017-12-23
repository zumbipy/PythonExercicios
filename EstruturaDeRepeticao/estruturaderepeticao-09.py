# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
09 - Faça um programa que imprima na tela apenas os números
ímpares entre 1 e 50.
"""
# ================================================================================
#                           Logica do Programa.
# ================================================================================
for i in range(1, 50):
    # Quando resto de uma divisao por 2 for 0 ele e par se nao e ímpar.
    if i % 2 != 0:
        print(i)
print("=" * 72)

# ou

for i in range(1, 50, 2):
    print(i)
