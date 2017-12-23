# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
12 - Desenvolva um gerador de tabuada, capaz de gerar a tabuada
de qualquer número inteiro entre 1 a 10. O usuário deve informar
de qual numero ele deseja ver a tabuada. A saída deve ser conforme
o exemplo abaixo:

Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
"""
# ================================================================================
#                           Variavel e Lógica do Programa.
# ================================================================================
numero = int(input("Digite o numero da tabuaba que deseja: "))

while True:
    # Verifica se o numero e menor que 0 ou maior 10 se for avisa um erro.
    if numero <= 0 or numero > 10:
        print("Numero Invalido!!!")
        numero = int(input("Digite um numero de 1 ao 10: "))
    else:
        for i in range(1, 11):
            print("{} X {:<3}= {:>3}".format(numero, i, i * numero))
        break
