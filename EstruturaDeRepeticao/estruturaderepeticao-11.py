# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
11 - Altere o programa anterior para mostrar no final a soma dos números.
"""
# ================================================================================
#                           Variaveis do Programa.
# ================================================================================
numero1 = int(input("Digite o inicio da contagem: "))
numero2 = int(input("Digite o final da contagem: "))
soma = 0

# ================================================================================
#                           Logica do Programa.
# ================================================================================

for i in range(numero1, numero2 + 1):
    # Soma vai se sempre ela mesmo mais o numero gerado.
    soma += i
print("Soma dos numeros gerados é {}".format(soma))
