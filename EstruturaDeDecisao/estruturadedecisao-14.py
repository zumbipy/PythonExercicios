# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
14 - Faça um programa que lê as duas notas parciais obtidas por um
aluno numa disciplina ao longo de um semestre, e calcule a sua média.
A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito
correspondente e a mensagem “APROVADO” se o conceito
for A, B ou C ou “REPROVADO” se o conceito for D ou E
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
# Entrada de Dados.
nota_1 = float(input("Digite a nota 1: "))
nota_2 = float(input("Digite a nota 2: "))

# Variaves
media = (nota_1 + nota_2) / 2
conceito = ""
final_avaliacao = ""

# ================================================================================
#                           Logica do programa
# ================================================================================
if media <= 4.0:
    conceito = "E"
    final_avaliacao = "REPROVADO"

elif media <= 6.0:
    conceito = "D"
    final_avaliacao = "REPROVADO"

elif media <= 7.5:
    conceito = "C"
    final_avaliacao = "APROVADO"

elif media <= 9.0:
    conceito = "B"
    final_avaliacao = "APROVADO"

else:
    conceito = "A"
    final_avaliacao = "APROVADO"

print('''
Nota 1:         {}
Nota 2:         {}
Media:          {}
Correspondente: {}
Status:         {}
'''.format(nota_1, nota_2, media, conceito, final_avaliacao))
