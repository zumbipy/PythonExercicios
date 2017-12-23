# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
12 - Faça um programa para o cálculo de uma folha de pagamento, sabendo
que os descontos são do Imposto de Renda, que depende do salário bruto
(conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde
a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade
de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a
quantidade de hora é 220.
saidas:
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
# Entrada de Dados.
valor_hora_trabalhada = float(input("Valor da hora trabalhada: "))
quantidade_hora_trabalhada = int(input("Digite as horas trabalhadas: "))

# Variáveis
salario_bruto = valor_hora_trabalhada * quantidade_hora_trabalhada
desconto = 0
fgts = salario_bruto * 0.11
inss = salario_bruto * 0.10
ir = 0

# ================================================================================
#                           Logica do programa
# ================================================================================
# Comparaçoes
if salario_bruto <= 900:
    desconto = 0
    ir = "00"

elif salario_bruto <= 1500:
    desconto = salario_bruto * 0.05
    ir = "05"

elif salario_bruto <= 2500:
    desconto = salario_bruto * 0.1
    ir = "10"

else:
    desconto = salario_bruto * 0.2
    ir = "20"

print('''        Salário Bruto:                  : R$  {:.2f}
        (-) IR   ({}%)                  : R$  {:.2f}
        (-) INSS (10%)                  : R$  {:.2f}
        FGTS     (11%)                  : R$  {:.2f}
        Total de descontos              : R$  {:.2f}
        Salário Liquido                 : R$  {:.2f}
'''.format(salario_bruto, ir, desconto, inss, fgts, inss + desconto,
           salario_bruto - (inss + desconto)))
