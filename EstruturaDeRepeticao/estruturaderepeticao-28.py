# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
28 - Faça um programa que calcule o valor total investido por um
colecionador em sua coleção de CDs e o valor médio gasto em cada um
deles. O usuário deverá informar a quantidade de CDs e o valor para
em cada um.
"""
# ================================================================================
#                                   Variaveis.
# ================================================================================
quantidade_cd = int(input("Quantidade de CDS: "))
valor_cd = 0
media = 0
valor_total_cd = 0

# ================================================================================
#                                   Logica.
# ================================================================================
for valor in range(quantidade_cd):
    valor_cd = float(input("Digite o valor {} de {} Cds.: ".format(
        valor + 1, quantidade_cd)))
    media += 1
    valor_total_cd += valor_cd

media = valor_total_cd / media
print("Valor médio de colenção foi %.2f " % media)
