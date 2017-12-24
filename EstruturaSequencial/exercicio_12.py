# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
12 - Tendo como dados de entrada a altura de uma pessoa, construa um
algoritmo que calcule seu peso ideal, usando a seguinte
fórmula: (72.7*altura) - 58
"""

altura = float(input("Digite sua altura sem cm: "))

peso_ideal = 72.7 * (altura / 100) - 58

print("Sua altura é {:.0f} entao seu peso ideal é {:.1f}".format(
    altura, peso_ideal))
