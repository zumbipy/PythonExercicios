# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 25/12/2017
"""
33 - O Departamento Estadual de Meteorologia lhe contratou para
desenvolver um programa que leia as um conjunto indeterminado de
temperaturas, e informe ao final a menor e a maior temperaturas
informadas, bem como a média das temperaturas.
"""

maximo = 0
minimo = 0
media = 0
contado = 0
temperaturas = None

while True:
    temperaturas = input("Digite a temperatura ou C para sair: ").lower()
    if temperaturas == "c":
        break
    temperaturas = int(temperaturas)
    if temperaturas >= maximo:
        maximo = temperaturas

    if temperaturas <= minimo:
        minimo = temperaturas
    media += temperaturas
    contado += 1

print(f"""
    Temperatura minima é: {minimo}
    Temperatura máxima é: {maximo}
    Temperatura média é: {media / contado}

    """)
