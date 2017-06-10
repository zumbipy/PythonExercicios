# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaDeDecisao
# Para execurta o programa on line entra no link a baixo:
# https://repl.it/I0mU/0
"""
10 - Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
ou "Valor Inválido!", conforme o caso.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
# Entrada de Dados.
turno = input('''Qual turno você estuda?
    M - matutino.
    V - Vespertino.
    N - Noturno.
Digite aqui: ''').lower()

m = "matutiono"
v = "vespertino"
n = "noturno"

# ================================================================================
#                           Logica do programa
# ================================================================================
# Comparando entrada com as opções.
if turno == "m":
    print("Bom Dia!")
elif turno == "v":
    print("Boa Tarde!")
elif turno == "n":
    print("Boa Noite!")
else:
    print("Valor Inválido!")
