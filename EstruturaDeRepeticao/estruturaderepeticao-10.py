# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
10 - Faça um programa que receba dois números inteiros e
gere os números inteiros que estão no intervalo compreendido
por eles.
"""
# ================================================================================
#                           Variaveis e Logica do Programa.
# ================================================================================
numero1 = int(input("Digite o inicio da contagem: "))
numero2 = int(input("Digite o final da contagem: "))

for i in range(numero1, numero2 + 1):
    print(i)
