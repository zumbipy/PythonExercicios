# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
4 - Supondo que a população de um país A seja da ordem de 80000 habitantes
com uma taxa anual de crescimento de 3% e que a população de B seja 200000
habitantes com uma taxa de crescimento de 1%. Faça um programa que
calcule e escreva o número de anos necessários para que a população do país
A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
habitantes_a = 80000
habitantes_b = 200000
anos = 0

# ================================================================================
#                           Logica do programa
# ================================================================================
while habitantes_a <= habitantes_b:
    crescimento_p_a = 80000 * 0.03
    crescimento_p_b = 200000 * 0.01
    anos += 1
    habitantes_a, habitantes_b = habitantes_a + crescimento_p_a, habitantes_b + crescimento_p_b

print("Vai leva {} anos.".format(anos))

impr