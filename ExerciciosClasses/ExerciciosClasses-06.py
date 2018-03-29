# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___// dev 26/03/2018
"""
06 - Classe TV: Faça um programa que simule um televisor criando-o
como um objeto.
O usuário deve ser capaz de informar o número do canal e aumentar ou
diminuir o volume.
Certifique-se de que o número do canal e o nível do volume permanecem
dentro de faixas válidas.
"""


class TV(object):
    def __init__(self):
        self.volume = 0
        self.canal = 0
    
    def aumentar(self):
        if self.volume == 100:
            return "Max"
        else:
            self.volume += 1
            return self.volume
    
    def diminuir(self):
        if self.volume == 0:
            return "Min"
        else:
            self.volume -= 1
            return self.volume
    
    def canal_mais(self):
        if self.canal == 150:
            self.canal = 1
            return self.canal
        else:
            self.canal += 1
            return self.canal
            
    def canal_menos(self):
        if self.canal <= 1:
            self.canal = 150
            return self.canal
        else:
            self.canal -= 1
            return self.canal

tv = TV()

