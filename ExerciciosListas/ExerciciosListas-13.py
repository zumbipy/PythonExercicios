# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
13 - Faça um programa que receba a temperatura média de cada mês do ano
e armazene-as em uma lista. Após isto, calcule a média anual das
temperaturas e mostre todas as temperaturas acima da média anual, e em
que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 –
Fevereiro, . . . ).
"""
temperaturas_media_mes = []
mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril',
       'Maio', 'Junho', 'Julho', 'Agosto',
       'Setembro', 'Outubro', 'Novembro', 'Dezembro']
item = 0
media = 0
soma = 0


for i in mes:
    item = int(input("Digite a Media da temperadura do mês {:<10s}: ".format(i)))
    soma += item
    # Adicionar o item sempre na frente da lista.
    temperaturas_media_mes.insert(0, item)

# item agora virou um contador.
item = 0
media = soma / 12
print()
print("Ĺista dos messes do ano que a temperatuda estava acima da média anual.")
for i in temperaturas_media_mes:
    if i > media:
        print("{:>02d} - {:^10s} com temperadura de {}°".format(item + 1, mes[item], i))

    item += 1
