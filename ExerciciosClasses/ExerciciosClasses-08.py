# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___// dev 31/03/2018
"""
08 - Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho
(estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa
ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo
menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição.
Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
"""


class Macaco(object):
    def __init__(self, nome, estomago):
        self.nome = nome
        self.estomago = estomago

    def __repr__(self):
        return f"Nome: {self.nome}\nEstomago: {self.estomago}"

    def comer(self, comida):
        dict_comida = {"banana": 100, "maça": 50, "formiga": 10}

        if comida in dict_comida.keys():
            self.estomago += dict_comida[comida]
        else:
            print("Valor Inválido")
            print("Macaco pode come ... Banana, Maça ou Formiga")

    def ver_estomago(self):
        return self.estomago

    def digerir(self):
        self.estomago -= 20
        return self.estomago

macaco1 = Macaco("PyNoob", 78)
macaco2 = Macaco("PyZumbi", 20)
