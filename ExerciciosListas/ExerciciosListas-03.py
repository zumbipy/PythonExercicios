# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaLista
"""
03 - Faça um Programa que leia 4 notas, mostre as notas
e a média na tela.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
notas = []
notas_aluno = None
media = 0

# ================================================================================
#                           Logica do programa
# ================================================================================
for n in range(1, 5):
    notas_aluno = float(input("Digite {}/4 notas: ".format(n)))
    notas.append(notas_aluno)
    media += notas_aluno

print()
print("Valores das notas.")
for valor in range(1, 5):
    print("Nota {} foi : {}".format(valor, notas[valor - 1]))

print("Média foi {}".format(media / 4))
