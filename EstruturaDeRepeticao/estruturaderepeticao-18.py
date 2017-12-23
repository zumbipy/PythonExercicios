# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
18 - Faça um programa que, dado um conjunto de N números,
determine o menor valor, o maior valor e a soma dos valores.
"""
valor_total = 0
n_conjunto = []
while True:
    n_numero = input("Digite um numero ou (S) - sair: ").lower()
    if n_numero == "s":
        break
    else:
        n_numero = int(n_numero)
        n_conjunto.append(n_numero)
    valor_total += n_numero
n_conjunto.sort()
print("Maior numero da lista é {}".format(n_conjunto[len(n_conjunto) - 1]))
print("Menor numero da lista é {}".format(n_conjunto[0]))
print("Menor numero da lista é {}".format(valor_total))
