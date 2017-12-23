# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
8 - Faça um programa que leia 5 números e informe a soma e a média dos números.
"""
# ================================================================================
#                           Variaveis do Programa.
# ================================================================================
soma = 0
numero = 0

# ================================================================================
#                           Logica do Programa.
# ================================================================================
for i in range(5):
    numero = int(input("Digite numero {} de 5: ".format(i + 1)))
    soma += numero

print("A soma dos 5 numeros é {} e a média é {}".format(soma, soma / 5))
