# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___// dev 23/03/2018
"""
05 - Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
A classe deve possuir os seguintes atributos: número da conta, nome do correntista
e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor,
saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
"""


class ContaCorrente(object):
    def __init__(self, nome, numero_conta, saldo=0):
        self.nome = nome
        self.numero_conta = numero_conta
        self.saldo = saldo

    def muda_nome(self, novo_nome):
        self.nome = novo_nome

    def deposito(self, valor):
        self.saldo += valor
        return self.saldo

    def saque(self, valor):
        if self.saldo < valor:
            print("Saldo Isuficiente")
        else:
            self.saldo -= valor
            return self.saldo
