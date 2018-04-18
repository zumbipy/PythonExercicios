# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
1 - Faça um programa que peça uma nota, entre zero e dez.
    Mostre uma mensagem caso o valor seja inválido e continue pedindo
até que o usuário informe um valor válido.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
# Entrada de Dados.
nota = int(input("Digite uma nota entre 0 e 10: "))

# ================================================================================
#                           Lógica do programa
# ================================================================================
# Loop com While

while True:
    if nota >= 0 and nota < 11:
        print("Valor Válido!")
        break
    print("Valor inválido")
    nota = int(input("Digite uma nota entre 0 e 10: "))
