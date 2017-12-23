# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
25 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela
deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5
como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
sim = 1
nao = 0
soma = 0

# ================================================================================
#                           Logica do programa
# ================================================================================
# Pega a respota converte pra MAIUSCULO.
pergunta_1 = input("""    Telefonou para a vítima?
        Sim
        Nao
        Digite sua responta: """).lower()
# Compara responta com texto se for verdade soma mais 1 a variavel.
if pergunta_1 == "sim":
    soma += sim
else:
    soma += nao

pergunta_2 = input("""    Esteve no local do crime?
        Sim
        Nao:
        Digite sua responta: """).lower()
if pergunta_2 == "sim":
    soma += sim
else:
    soma += nao

pergunta_3 = input("""    Mora perto da vítima?
        Sim
        Nao:
        Digite sua responta: """).lower()
if pergunta_3 == "sim":
    soma += sim
else:
    soma += nao

pergunta_4 = input("""    Devia para a vítima?
        Sim
        Nao:
        Digite sua responta: """).lower()
if pergunta_4 == "sim":
    soma += sim
else:
    soma += nao

pergunta_5 = input("""    Já trabalhou com a vítima?
        Sim
        Nao:
        Digite sua responta: """).lower()
if pergunta_5 == "sim":
    soma += sim
else:
    soma += nao

# Comparação onde decide sem é ou não é o assasino.
if soma <= 2:
    print("classificada como \"Suspeito(a)\"")
elif soma <= 4:
    print("classificada como \"Cúmplice\"")
else:
    print("classificada como \"Assasino(a)\"")
