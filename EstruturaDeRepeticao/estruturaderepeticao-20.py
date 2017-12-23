# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
20 - Altere o programa de cálculo do fatorial, permitindo ao usuário
calcular o fatorial várias vezes e limitando o fatorial a números
inteiros positivos e menores que 16.
"""
# ================================================================================
#                                   Logica.
# ================================================================================
while True:
    a = 1
    b = 0
    n_esimo = int(input("Digite o n-ésmo termo: "))
    while True:
        # verifica se o valor esta nas condiçoes validas.
        if n_esimo >= 17 or n_esimo <= 0:
            print("!!! Numero Invalido !!!")
            n_esimo = int(input("Digite o n-ésmo termo: "))
        else:
            break
    # Loop para fazer o calculo.
    for i in range(n_esimo):
        c = a + b
        # aqui servi pra coloca '.' no ultimo termo.
        if (n_esimo - 1) > i:
            print("{}, ".format(c), end="")
        else:
            print("{}.".format(c))
        a, b = b, c
