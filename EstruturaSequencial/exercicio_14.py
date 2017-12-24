# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
14 - João Papo-de-Pescador, homem de bem, comprou um microcomputador
para controlar o rendimento diário de seu trabalho.
    Toda vez que ele traz um peso de peixes maior que o estabelecido
pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar
uma multa de R$ 4,00 porquilo excedente. João precisa que você faça
um programa que leia a variável peso (peso de peixes)
e verifique se há excesso. Se houver, gravar na variável excesso e na
variável multa o valor da multa que João deverá pagar. Caso contrário
mostrar tais variáveis com o conteúdo ZERO.
"""

peso_de_peixe = float(input("Digite o peso do peixe: "))
excesso = 0
multa = 0

if peso_de_peixe > 50:
    excesso = peso_de_peixe - 50
    multa = excesso * 4.00
    print("Exesso de peso: {:.0f}kg".format(excesso))
    print("Multa: {:.2f} reais".format(multa))
else:
    print("Exesso de peso: {}".format(excesso))
    print("Multa: {}".format(multa))
