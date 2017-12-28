# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 25/12/2017
"""
35 - Encontrar números primos é uma tarefa difícil. Faça um programa que gera
uma lista dos números primos existentes entre 1 e um número inteiro informado
pelo usuário.
"""
numero = int(input("Digite um número: "))
diviso = 1
lista_primos = []

for i in range(1, numero + 1):

    for n in range(1, i):
        if i % n == 0:
            diviso += 1
            if diviso > 2:
                break
    if diviso == 2:
        lista_primos.append(i)
    diviso = 1

print(lista_primos)
