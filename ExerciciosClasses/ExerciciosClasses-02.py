# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/ /dev 13/03/2018
"""
02 - Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""


class Quadrado(object):
    def __init__(self, tamano_do_lado=10):
        self.lados = tamano_do_lado

    def mudao_valor_lados(self, numero):
        self.lados = numero
        self.area = numero * 2
        return self.lados, self.area
