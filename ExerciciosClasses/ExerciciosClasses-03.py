# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___// dev 19/03/2018
"""
03 - Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades
de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e
de rodapés necessárias para o local.
"""


class Retangulo(object):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def troca(self):
        self.base = int(input("Digite a nova Base: "))
        self.altura = int(input("Digite a Altura: "))

    def valores(self):
        return f"Base: {self.base}\nAltura: {self.altura}"

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return (self.base * 2) + (self.altura * 2)

print("Programa Calcular Quantidade de pisos e de Rodapés. ")

base = int(input("Digite a Base: "))
altura = int(input("Digite a Altura: "))
print()

local = Retangulo(base, altura)

print(f"Valores do local:\n{local.valores()}", end="\n\n")
print(f"Quantidade de piso: {local.area()} m2")
print(f"Quantidade de rodapé: {local.perimetro()} m2")
