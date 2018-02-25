# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 25/02/2018
"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um
link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando
este link (em minutos).
"""
mb = int(input("Digite o total dos MB para baixa: "))
velocidade_down = int(input("Digite a velocidade do Donwlonad: "))

tempo_down = ((mb * velocidade_down) / 60)
print(f"Vai leva {tempo_down:,.2f} minutos".replace(".", ","))
