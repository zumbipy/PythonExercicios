# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
17 - Faça um programa que calcule o fatorial de um número inteiro
fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""
# ================================================================================
#                                       Variaveis.
# ================================================================================
numero = int(input("Digite um numero Inteiro: "))
# Um string que vai se somada depois.
final = "{0}!={0}.".format(numero)
valor = 0

# ================================================================================
#                                   Logica.
# ================================================================================
for i in range(numero, 1, -1):
    valor = numero * (i - 1)
    numero = valor
    # Este if so vai se verdade no ultimo loop.
    if 2 == i:
        # quando falso soma i= a final da str.
        final += "{}=".format(i - 1)
    else:
        # quando verdade soma i. a str
        final += "{}.".format(i - 1)

# depois q terminou tudo ele soma o valor a str.
final += "{}".format(valor)
print(final)
