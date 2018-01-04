# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 02/01/2018
"""
43 - O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral
do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.
"""

lista_pedido = []  # esta lista tera outra lista [codigo, quantidade, valor_total]
lista_produtos = [["Cachorro Quente", 100, 1.20],
                  ["Bauru Simples", 101, 1.30],
                  ["Bauru com ovo", 102, 1.50],
                  ["Hambúrguer", 103, 1.20],
                  ["Cheeseburguer", 104, 1.30],
                  ["Refrigerante", 105, 1.00]]

print("""Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00""")
valor_paga = 0
