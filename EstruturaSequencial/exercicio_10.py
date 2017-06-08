# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaSequencial
"""
10 - Faça um Programa que peça a temperatura em graus Celsius,
transforme e mostre em graus Farenheit.
"""

temp_celsius = int(input("Digite a temperadura em (Graus Celsius)°C: "))

farenheit = ((temp_celsius / 5) * 9 + 32)

print("Você digitou {}°C e igual a {:.0f}°F".format(temp_celsius, farenheit))
