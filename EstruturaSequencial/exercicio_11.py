# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaSequencial)
"""
10 - Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
"""

numero1 = int(input("Digite Um numero: "))
numero2 = int(input("Digite Outro numero: "))
n_real = float(input("Digite Outro numero: "))

respA = (numero1 * 2) * (numero2 / 2)
respB = numero1 * 3 + n_real
respC = n_real**3

print("O produto do dobro do primeiro com metade do segundo {}".format(
    respA))
print("A soma do triplo do primeiro com o terceiro {}".format(respB))
print("o terceiro elevado ao cubo {}".format(respC))
