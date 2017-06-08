# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaDeRepeticao
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
