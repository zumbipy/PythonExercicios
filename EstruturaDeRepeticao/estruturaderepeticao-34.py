# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 25/12/2017
"""
35 - Os números primos possuem várias aplicações dentro da Computação, por exemplo na
Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo.
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
"""

numero = int(input("Digite um número: "))
diviso = 0

for n in range(1, numero + 1):
    if numero % n == 0:
        diviso += 1

if diviso == 2:
    print("Primo")
else:
    print("Não primo")
