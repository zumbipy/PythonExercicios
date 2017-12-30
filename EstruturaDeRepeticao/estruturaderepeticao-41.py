# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 30/12/2017
"""
41 - Faça um programa que receba o valor de uma dívida e mostre uma tabela com os
seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
"""
l_parcelas_juros = [[1, 0], [3, 0.10], [6, 0.15], [9, 0.20], [12, 0.25]]
valor_divida = int(input("Digite o valor da divida: "))
valor_pacela = 0
valor_do_juros = 0
valor_apagar = valor_divida

print(f"""
+-----------------+-----------------+------------------------+------------------+
| Valor da Dívida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela |
+-----------------+-----------------+------------------------+------------------+""")

for parcelas in range(5):

    valor_do_juros = valor_divida * l_parcelas_juros[parcelas][1]
    valor_apagar += valor_do_juros
    valor_pacela = valor_apagar / l_parcelas_juros[parcelas][0]

    print(f"|{valor_apagar:<17.0f}|{valor_do_juros:<17.0f}|{l_parcelas_juros[parcelas][0]:<24}|{valor_pacela:<18.0f}|")
    valor_apagar = valor_divida  # resetando a variavle pra o valor inicial.

print("+-----------------+-----------------+------------------------+------------------+")
