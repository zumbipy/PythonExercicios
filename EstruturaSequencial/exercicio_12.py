# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaSequencial
"""
12 - Tendo como dados de entrada a altura de uma pessoa, construa um
algoritmo que calcule seu peso ideal, usando a seguinte
fórmula: (72.7*altura) - 58
"""

altura = float(input("Digite sua altura sem cm: "))

peso_ideal = 72.7 * (altura / 100) - 58

print("Sua altura é {:.0f} entao seu peso ideal é {:.1f}".format(
    altura, peso_ideal))
