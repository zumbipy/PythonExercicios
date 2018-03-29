# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___// dev 20/03/2018
"""
04 - Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer.
Obs: Por padrão, a cada ano que nossa pessoa envelhece,
sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""


class Pessoa(object):
    def __init__(self, nome, idade, peso, altura):
        self.idade = idade
        self.nome = nome
        self.peso = peso
        self.altura = altura

    def __repr__(self):
        return f"Nome: {self.nome}\nIdade:{self.idade}\nPeso:{self.peso}\nAltura:{self.altura}"

    @staticmethod
    def positivo(numero):
        if numero < 0:
            return False
        else:
            return True

    def envelhercer(self, idade):
        if self.positivo(idade):
            if idade < 21:
                self.altura += idade * 0.5
                self.idade += idade
            else:
                self.idade += idade

    def engordar(self, peso):
        if self.positivo(peso):
            print("Valor Invalido!!!")
        else:
            self.peso += peso

    def emagrecer(self, peso):
        if self.positivo(peso):
            print("Valor Invalido!!!")
        else:
            self.peso -= peso

    def crescer(self, altura):
        if self.positivo(altura):
            self.altura += altura
        else:
            print("Valor Invalido!!!")


pynoob = Pessoa("Noob", 10, 49, 130)

print(pynoob)
