# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
9 - Faça um Programa que peça a temperatura em graus Farenheit,
transforme e mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9).
"""

temp_graus = int(input("Digite a temperuda em \"Graus Farenheit\" (°F): "))

c = (5 * (temp_graus - 32) / 9)

print("{}°F e igual a {:.0f}°C".format(temp_graus, c))
