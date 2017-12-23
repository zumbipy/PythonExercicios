# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
27 - Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a
quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo
cliente.
"""
# ================================================================================
#                           Print da tabela do programa
# ================================================================================
print("""+======================================================+
|               Tabela de preço                        |
+======================================================+
|                      Até 5 Kg           Acima de 5 Kg|
|Morango         R$ 2,50 por Kg          R$ 2,20 por Kg|
|Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg|
+======================================================+
|Acima de 8 kg ou compra mais de R$25,desconto de 10%  |
+======================================================+""")

# ================================================================================
#                           Variaveis do Programa
# ================================================================================
# Comandos de entrada
morango = float(input("Digite a quantidade de quilos de \"Morango\" em Kg: "))
maca = float(input("Digite a quantidade de quilos de \"Maça\" em Kg: "))

# ================================================================================
#                           Inicio do programa
# ================================================================================
# Variaveis, Comparaçoes e Abribuição dos valores da tebela de preço.
# Aqui uso um if else em uma linha só.
mg_valor = 2.50 if morango <= 5 else 2.20
mc_valor = 1.80 if maca <= 5 else 1.50

valor_total_mg = mg_valor * morango
valor_total_mc = mc_valor * maca
valor_total_cp = valor_total_mc + valor_total_mg

# Comparaçoes de valores com ou sem desconto do Morango.
if morango > 8 or valor_total_cp > 25:
    desconto = valor_total_mg * 0.10
    print("Voce comprou {:.0f} kg e vai pagar R$: {:.2f} já com desconto de R$: {:.2f} (10%).".
          format(morango, valor_total_mg - desconto, desconto))
else:
    print("Voce comprou {:.0f} kg e vai pagar R$: {:.2f}.".
          format(morango, valor_total_mg))

# Comparaçoes de valores com ou sem desconto da Maça.
if maca > 8 or valor_total_cp > 25:
    desconto = valor_total_mc * 0.10
    print("Voce comprou {:.0f} kg e vai pagar R$: {:.2f} já com desconto de R$: {:.2f} (10%).".
          format(maca, valor_total_mc - desconto, desconto))
else:
    print("Voce comprou {:.0f} kg e vai pagar R$: {:.2f}.".
          format(maca, valor_total_mc))
