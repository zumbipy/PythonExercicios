
# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaLista
"""
14 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a
participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela
deve ser classificada como "Suspeita", entre 3 e 4 como como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""
l_perguntas = ['a. Telefonou para a vítima?', 'b. Esteve no local do crime?',
               'c. Mora perto da vítima?', 'd. Devia para a vítima?',
               'e. Já trabalhou com a vítima?']
l_classificado = ["Inocente", "Suspeita", "Suspeita", "Cúmplice", "Cúmplice", "Assassino"]
contado_de_sim = 0
r = None

for pergunta in l_perguntas:
    r = input("{}: (S) - Sim ou (N) - Não: ".format(pergunta)).lower()
    print()

    # validação simples.
    while True:
        if r == "s" or r == "n":
            break
        else:
            print("Digite S ou N !!!")
            r = input("{}: (S) - Sim ou (N) - Não: ".format(pergunta), end="\n" * 2).lower()

    if r == 's':
        contado_de_sim += 1

print("Você foi classificado como {}.".format(l_classificado[contado_de_sim]))
