# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 25/12/2017
"""
32 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
usuário.
Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
"""

fatorial = int(input("Digite um numero: "))
total = 1
saida_str = f"{fatorial}! = "
for numero in range(fatorial, 0, -1):
    print(numero)
    if numero > 1:
        total = total * numero
        saida_str += f" {numero}."
    else:
        saida_str += f" {numero}"

print(f"{saida_str} = {total}")
