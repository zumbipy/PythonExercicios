# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
21 - Faça um programa que peça um número inteiro e determine se ele
é ou não um número primo. Um número primo é aquele que é divisível
somente por ele mesmo e por 1.
"""
# ================================================================================
#                                      Variavel.
# ================================================================================
numero = int(input("Digite um numero: "))
contado_zero = 0

# ================================================================================
#                                      Logica.
# ================================================================================
# Unico numero primo par e o 2.
if numero == 2:
    print("É um numero PRIMO")

# 1 não e primo.
elif numero <= 1:
    print("Não e um numero primo")
else:
    """
        Quando dividimos um numero e da zero o numero usando e divisor, então
    se tive mais que dois modulos que de 0 o numero já não e primo pq ele so
    pode se divido por 1 e por ele mesmo.
    ex:
        '5 % 1 = 0'
        5 % 2 = 1
        5 % 3 = 2
        5 % 4 = 1
        '5 % 5 = 0'
    """
    for numeros in range(1, numero + 1):
        if numero % numeros == 0:
            contado_zero += 1
        # Otimização da divisoes, dica dada pela Nayra Oliveira.
        if contado_zero > 2:
            print("Numero {} não é primo".format(numero))
            break
    else:
        print("Numero {} é primo".format(numero))
