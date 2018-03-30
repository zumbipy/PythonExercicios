# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___// dev 30/03/2018
"""
07 - Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
Atributos: Nome, Fome, Saúde e Idade b.
Métodos: Alterar Nome, Fome, Saúde e Idade;
Retornar Nome, Fome, Saúde e Idade
Obs: Existe mais uma informação que devemos levar em consideração,
o Humor do nosso tamagushi, este humor é uma combinação entre os atributos
Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo
para armazenar esta informação por que ela pode ser calculada a qualquer momento.
"""


class Tamagushi(object):
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.ffome = fome
        self.ssaude = saude
        self.iidade = idade
        self.hhumor = self.humor()

    def troca_nome(self):
        self.nome = input("Digite o Novo nome: ")
        print(f"Novo nome Alterando com Sucesso!")
        return self.infor()

    def fome(self, numero):
        if self.valida_faixar(numero):
            self.ffome = numero
        else:
            print("Valor Inválido")
        return self.infor()

    def idade(self, numero):
        if numero < 0:
            return "Valor Inválido "
        self.iidade += numero
        return self.infor()

    def saude(self, numero):
        if self.valida_faixar(numero):
            self.ssaude = numero
        else:
            return "Valor Inválido!!!"
        return self.infor()

    def infor(self):
        infor = f"""Nome: {self.nome}
Fome: {self.ffome}
Idade: {self.iidade}
Saúde: {self.ssaude}
Humor: {self.humor()}"""
        print(infor)

    def valida_faixar(self, numero):
        valor_max = 101
        valor_min = -1
        if numero >= valor_max:
            return False
        if numero <= valor_min:
            return False
        return True

    def humor(self):
        hhumor = (self.ffome + self.ssaude) // 2
        print(hhumor)
        if hhumor <= 25:
            return "Triste"
        elif hhumor <= 50:
            return "Normal"
        elif hhumor <= 75:
            return "Feliz"
        elif hhumor >= 100:
            return "Super Feliz"


ka = Tamagushi("Test", 100, 100, 1)
ka.infor()
