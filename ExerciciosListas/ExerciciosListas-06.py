# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaLista
"""
06 - Faça um Programa que peça as quatro notas de 10 alunos, calcule e
armazene num vetor a média de cada aluno, imprima o número de alunos
com média maior ou igual a 7.0.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
notas_aluno = None
v_media_aluno = []
a_aprovados = 0
media = None
total_nota = 0

# ================================================================================
#                           Logica do programa
# ================================================================================
# For dentro de for.
for alunos in range(1, 3):
    print("Notas do Aluno {}.".format(alunos))
    for notas in range(1, 5):
        notas_aluno = float(input("Digite a nota {}/4: ".format(notas)))
        total_nota += notas_aluno
    print()
    media = total_nota / 4
    v_media_aluno.append(media)
    # Resertando Variavel.
    total_nota = 0

# Verificação de Notas
for n in v_media_aluno:
    if n >= 7:
        a_aprovados += 1

print("Números de alunos com nota igual ou maior que 7 foi: ", a_aprovados)
