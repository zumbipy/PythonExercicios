# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
13 - Faça um programa que peça dois números, base e expoente,
calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.
"""
# ================================================================================
#                           Vaiaveis do Programa.
# ================================================================================
numero1 = int(input("Numero da base: "))
numero2 = int(input("Numero do expoente: "))
potencia = 0

# ================================================================================
#                           Logica do Programa.
# ================================================================================
if numero2 == 0:
    print("Resultado é 1")
elif numero2 == 1:
    print("Resultado é", numero1)
else:
    # potencia vira base.
    potencia = numero1
    for i in range(1, numero2):
        potencia = numero1 * potencia
    print("Resultado é {}".format(potencia))
