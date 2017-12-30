# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 30/12/2017
"""
39 - Faça um programa que leia dez conjuntos de dois valores, o primeiro representando
o número do aluno e o segundo representando a sua altura em centímetros.
Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o
número do aluno mais baixo, junto com suas alturas.
"""
from random import randint as gerar

lista_alunos = []
mais_baixo = 0, 999  # Neste caso usei tuplas para resolver o programa.
mais_alto = 0, 0


for resgistra in range(1, 11):
    numero_aluno = resgistra  # ou int(input("Digite numero do aluno: "))
    altura_aluno = gerar(130, 310)  # ou int(input("Digite altura do aluno: "))
    print(f"Numero do aluno: {numero_aluno} | Altura: {altura_aluno}")
    lista_alunos.append([numero_aluno, altura_aluno])

for verificar in lista_alunos:
    aluno, altura = verificar
    if altura > mais_alto[1]:
        mais_alto = aluno, altura

    if altura < mais_baixo[1]:
        mais_baixo = aluno, altura

print(f"O Aluno {mais_alto[0]} foi mais alto com {mais_alto[1]} cm")
print(f"O Aluno {mais_baixo[0]} foi mais baixo com {mais_baixo[1]} cm")
