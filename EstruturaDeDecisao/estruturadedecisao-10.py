# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
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
