# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
27 - Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para
cada turma. As turmas não podem ter mais de 40 alunos.
"""
# ================================================================================
#                              Variaveis
# ================================================================================
quantidade_turmas = int(input("Digite a quantidade de turmas: "))
quantidade_alunos = 0
media = 0
total = 0

# ================================================================================
#                             Logica.
# ================================================================================
for turmas in range(quantidade_turmas):
    quantidade_alunos = int(input("Digite a quantidade de alunos da turma {} de {}: ".format(
        turmas + 1, quantidade_turmas)))
    while True:
        if quantidade_alunos >= 40:
            print("Digite um numero menor que 40!!!")
            quantidade_alunos = int(input("Digite a quanidade de Alunos: "))
        else:
            break
    total += quantidade_alunos
    media += 1
media = total / media
print(media)
