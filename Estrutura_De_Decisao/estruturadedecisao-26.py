# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaDeDecisao
# Para execurta o programa on line entra no link a baixo:
# https://repl.it/I28H/1
"""
26 - Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3%.
acima de 20 litros, desconto de 5%.
Gasolina:
até 20 litros, desconto de 4%.
acima de 20 litros, desconto de 6%.
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do
litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
tipo_combustivel = input("Digite A-álcool(R$: 1,90) ou G-gasolina(R$: 2,50): "
                         ).lower()
litros_comprados = int(input("Vai compra quantos litros?: "))
p_alcool = 1.90
p_gasolina = 2.50

# ================================================================================
#                           Logica do programa
# ================================================================================
if "alcool".startswith(tipo_combustivel):
    if litros_comprados <= 20:
        desconto = (litros_comprados * p_alcool) * 0.03
        valor_total = (litros_comprados * p_alcool) - desconto
        print("""Você gastou     {:.2f}.
Seu descontro é {:.2f}.
Valor total é   {:.2f}.""".format(litros_comprados * p_alcool, desconto,
                                  valor_total))
    else:
        desconto = (litros_comprados * p_alcool) * 0.05
        valor_total = (litros_comprados * p_alcool) - desconto
        print("""Você gastou     {:.2f}.
Seu descontro é {:.2f}.
Valor total é   {:.2f}""".format(litros_comprados * p_alcool, desconto,
                                 valor_total))

elif "gasolina".startswith(tipo_combustivel):
    if litros_comprados <= 20:
        desconto = (litros_comprados * p_gasolina) * 0.04
        valor_total = (litros_comprados * p_gasolina) - desconto
        print("""Você gastou     {:.2f}.
Seu descontro é {:.2f}.
Valor total é   {:.2f}""".format(litros_comprados * p_gasolina, desconto,
                                 valor_total))
    else:
        desconto = (litros_comprados * p_gasolina) * 0.06
        valor_total = (litros_comprados * p_gasolina) - desconto
        print("""Você gastou     {:.2f}.
Seu descontro é {:.2f}.
Valor total é   {:.2f}""".format(litros_comprados * p_gasolina, desconto,
                                 valor_total))
