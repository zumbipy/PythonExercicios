# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
11 - As Organizações Tabajara resolveram dar um aumento de salário aos
seus colaboradores e lhe contraram para desenvolver o programa que
calculará os reajustes.

    Faça um programa que recebe o salário de um colaborador e o reajuste
segundo o seguinte critério, baseado no salário atual:

salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento se
realizado, informe na tela:

o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
# Entrada de Dados.
salario_colaborador = float(input("Digite o salario do Coloborador: "))
salario_final = 0
porcentagem = 0
aumento = 0

# Calculos dos Reajuste
aumento_20 = salario_colaborador * 0.20
aumento_15 = salario_colaborador * 0.15
aumento_10 = salario_colaborador * 0.10
aumento_5 = salario_colaborador * 0.05

# ================================================================================
#                           Logica do programa
# ================================================================================

if salario_colaborador <= 280:
    salario_final = salario_colaborador + aumento_20
    porcentagem = "20%"
    aumento = aumento_20

elif salario_colaborador <= 700:
    salario_final = salario_colaborador + aumento_15
    porcentagem = "15%"
    aumento = aumento_15

elif salario_colaborador < 1500:
    salario_final = salario_colaborador + aumento_10
    porcentagem = "10%"
    aumento = aumento_10

else:
    salario_final = salario_colaborador + aumento_5
    porcentagem = "5%"
    aumento = aumento_5

print('''
o salário antes do reajuste é R$    {:.2f}
o percentual de aumento aplicado:   {}
o valor do aumento é R$             {:.2f}
o novo salário, após o aumento é R$ {:.2f}
'''.format(salario_colaborador, porcentagem, aumento, salario_final))
