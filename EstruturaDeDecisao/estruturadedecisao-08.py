# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
8 - Faça um programa que pergunte o preço de três produtos e informe
qual produto você deve comprar, sabendo que a decisão é sempre pelo
mais barato.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
# Entrada de Dados.
prod0 = float(input("Digite o valor do produto 1: "))
prod1 = float(input("Digite o valor do produto 2: "))
prod2 = float(input("Digite o valor do produto 3: "))

# ================================================================================
#                           Logica Do Programa
# ================================================================================
# Comparaçoes pra sabe qual e o menor produto entre os 3 digitados.
if prod0 <= prod1 <= prod2:
    print("""O mais barato é o produto {}.
Seu valor é R$:{:.2f}""".format("produto 1", prod0))

elif prod0 <= prod1 >= prod2 > prod0:
    print("""O mais barato é o produto {}.
Seu valor é R$:{:.2f}""".format("produto 1", prod0))

elif prod0 >= prod1 <= prod2 <= prod1:
    print("""O mais barato é o produto {}.
Seu valor é R$:{:.2f}""".format("produto 2", prod1))

elif prod0 <= prod1 >= prod2 <= prod1:
    print("""O mais barato é o produto {}.
Seu valor é R$:{:.2f}""".format("produto 3", prod2))

elif prod0 >= prod1 >= prod2:
    print("""O mais barato é o produto {}.
Seu valor é R$:{:.2f}""".format("produto 3", prod2))

elif prod0 >= prod1 <= prod2:
    print("""O mais barato é o produto {}.
Seu valor é R$:{:.2f}""".format("produto 2", prod1))
