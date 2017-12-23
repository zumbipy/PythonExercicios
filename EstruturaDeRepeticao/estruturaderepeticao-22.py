# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
22 - Altere o programa de cálculo dos números primos, informando,
caso o número não seja primo, por quais número ele é divisível.
"""
# ================================================================================
#                                      Variavel.
# ================================================================================
numero = int(input("Digite um numero: "))
contado_zero = 0
divisor = ""
# ================================================================================
#                                      Logica.
# ================================================================================
if numero == 2:
    print("Numero 2 primo e é divisevel por 1, 2.")

# 1 não e primo.
elif numero <= 1:
    print("Não e um numero primo")
    print("Ele e dividivel so por ele mesmo.")
else:

    for numeros in range(1, numero + 1):
        if numero % numeros == 0:
            # aqui e adcionado o numero divisivel a varivaln srt
            if numeros == numero:
                divisor += "{}. ".format(numeros)
            else:
                divisor += "{}, ".format(numeros)
            contado_zero += 1
    if contado_zero > 2:
        print("Numero {} não é primo e ele e divisivel por {}".format(
            numero, divisor))
    else:
        print("Numero {} é primo".format(numero))
