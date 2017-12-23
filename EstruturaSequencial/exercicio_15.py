# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaSequencial
"""
15 - Faça um Programa que pergunte quanto você ganha por hora e o número
de horas trabalhadas no mês. Calcule e mostre o total do seu salário no
referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo
saida:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
"""

reais_horas = float(input("Quanto você ganha por Hora?: "))
horas_mes = float(input("Quantas horas você trabalhou este mês?: "))
print("\n")
salario_bruto = reais_horas * horas_mes
salario_descontado = salario_bruto


ir = salario_descontado * 0.11
salario_descontado -= ir

inss = salario_descontado * 0.08
salario_descontado -= inss

sindicato = salario_descontado * 0.05
salario_descontado -= sindicato

print("Salário Bruto: {:.2f} R$".format(salario_bruto))
print("IR (11%): {:.2f} R$".format(ir))
print("INSS (8%): {:.2f} R$".format(inss))
print("Sindicato ( 5%): {:.2f} R$".format(sindicato))
print("Salário Liquido : {:.2f} R$".format(salario_descontado))
