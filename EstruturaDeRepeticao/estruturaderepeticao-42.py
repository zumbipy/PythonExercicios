# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 02/01/2018
"""
42 - Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos
deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados
deverá terminar quando for lido um número negativo.
"""
lista_intervalos = [["[0-25]", 0], ["[26-50]", 0], ["[51-75]", 0], ["[76-100]", 0]]

while True:
    numero_positivo = int(input("Digite numero positivos ou negativo para sair: "))
    if numero_positivo < 0:
        break
    if numero_positivo >= 0 and numero_positivo <= 25:
        lista_intervalos[0][1] += 1

    if numero_positivo >= 26 and numero_positivo <= 50:
        lista_intervalos[1][1] += 1

    if numero_positivo >= 51 and numero_positivo <= 75:
        lista_intervalos[2][1] += 1

    if numero_positivo >= 76 and numero_positivo <= 100:
        lista_intervalos[3][1] += 1

for dados in lista_intervalos:
    intervalos, numeros = dados
    print(f"No intervalos {intervalos} tem {numeros} numeros.")
