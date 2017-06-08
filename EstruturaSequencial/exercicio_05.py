# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaSequencial
# 5 - Faça um Programa que converta metros para centímetros.

metros = float(input("Digite quantos metros você quer converter: "))

print("Você Digitou {:.0f}M que é igual à {:.0f}cm".format(
    metros, metros * 100))
