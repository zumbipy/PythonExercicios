# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
14 - Faça um programa que peça 10 números inteiros,
calcule e mostre a quantidade de números pares e a quantidade de
números impares.
"""
# ================================================================================
#                               Variaveis
# ================================================================================
numero = 0
pares = 0
impares = 0

# ================================================================================
#                               Lógica.
# ================================================================================
for i in range(1, 11):
    numero = int(input("Digite numero {} de 10: ".format(i)))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("""Total de numero pares é {} e o de numeros impares é {}
    """.format(pares, impares))
