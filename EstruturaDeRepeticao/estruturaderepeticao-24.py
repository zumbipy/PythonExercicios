# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
24 - Faça um programa que calcule o mostre a média aritmética de N notas.
"""
notas = None
media = 0
total_notas = 0
print("Para sair digite S - sair")
while True:
    perguta = input("Digite as notas: ").lower()
    if perguta == "s":
        break
    else:
        notas = float(perguta)
    total_notas += notas
    media += 1

print(total_notas / media)
