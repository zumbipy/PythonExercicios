# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaSequencial
"""
9 - Faça um Programa que peça a temperatura em graus Farenheit,
transforme e mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9)."""

temp_graus = int(input("Digite a temperuda em \"Graus Farenheit\" (°F): "))

c = (5 * (temp_graus - 32) / 9)

print("{}°F e igual a {:.0f}°C".format(temp_graus, c))
