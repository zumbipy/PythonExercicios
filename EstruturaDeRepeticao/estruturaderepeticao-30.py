# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
30 - O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende
implantar a metodologia da tabelinha, que já é um sucesso na sua
loja de 1,99. Você foi contratado para desenvolver o programa que monta
a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão
informado pelo usuário, conforme o exemplo abaixo:
Preço do pão: R$ 0.18
Panificadora Pão de Ontem - Tabela de preços
1 - R$ 0.18
2 - R$ 0.36
...
50 - R$ 9.00

"""

valor_pao = float(input("Digite o valor do Preço do pão: "))

for tabela in range(1, 51):
    preco = tabela * valor_pao
    print("{:<2} - R$ {:.2f}".format(tabela, preco))
