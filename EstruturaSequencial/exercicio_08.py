# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaSequencial
"""
 8 - Faça um Programa que pergunte quanto você ganha por hora e o número
de horas trabalhadas no mês. Calcule e mostre o total do seu salário no
referido mês.
"""
ganho_por_hora = float(input("Quanto você por hora? "))
horas_trabalhadas = float(input("Quantas Horas você trabalhou este mês? "))

print("""Você recebe {:.2f} por hora.
Trabalhou {:.0f} horas por mes.
Entao você vai recebe {:.2f} reais.
""".format(ganho_por_hora,
           horas_trabalhadas, ganho_por_hora * horas_trabalhadas))
