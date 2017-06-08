# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaSequencial
"""
16 - Faça um programa para uma loja de tintas. O programa deverá pedir
o tamanho em metros quadrados da área a ser pintada. Considere que a
cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta
é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário
a quantidades de latas de tinta a serem compradas e o preço total.
"""

metro_quadrados = int(input("Digite quantos metros você deseja pinta: "))
valor_lata_18_litros = 80
litros = metro_quadrados // 3
total_de_litros = litros / 18

if total_de_litros % 3 == 0:
    print("Total de latas é {}".format(1))
    print("Valor que você vai paga: R$ {:.2f} reais".format(
        valor_lata_18_litros))
else:
    print("Total de latas é {}".format(round(total_de_litros)))
    print("Valor que você vai paga: R$ {:.2f} reais".format(
        valor_lata_18_litros * round(total_de_litros)))
