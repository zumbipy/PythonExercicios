# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
16 - Faça um programa para uma loja de tintas. O programa deverá pedir
o tamanho em metros quadrados da área a ser pintada. Considere que a
cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta
é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário
a quantidades de latas de tinta a serem compradas e o preço total.
"""
metros_quadrados = int(input("Quantos metros quadrados você quer compra: "))
total_litros = metros_quadrados * 3
total_latas = total_litros / 18
print(total_latas)
