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

dicionario_pedido = {}  # esta dicionario tera {"prduto":{"quantidade': 0 "valor":0, "codigo": 0}}
dicionario_produtos = {100: {"produto": "Cachorro Quente", "valor": 1.20},
                       101: {"produto": "Bauru Simples", "valor": 1.30},
                       102: {"produto": "Bauru com ovo", "valor": 1.50},
                       103: {"produto": "Hambúrguer", "valor": 1.20},
                       104: {"produto": "Cheeseburguer", "valor": 1.30},
                       105: {"produto": "Refrigerante", "valor": 1.00}
                       }
valor_paga = 0
codigo_pedido = None
quantidade = None
valor_produto = None

# Sainda da tela do codigo
print('''+------------------+----------+-------------+
| Especificação    | Código   | Preço       |
+------------------+----------+-------------+''')

for saida_tela in dicionario_produtos:
    produto, valor = dicionario_produtos[saida_tela].values()
    codigo = saida_tela
    print(f"| {produto:<16} | {codigo:^8} | R$: {valor:>7.2f} |")
print("+------------------+----------+-------------+")


# Logica do pedido.
while True:
    codigo_pedido = str(input("Digite o Codigo do Produto ou (S) para sair: ")).lower()
    if codigo_pedido == "s":
        break
    else:
        codigo_pedido = int(codigo_pedido)

    # Validação do codigo do produto
    if codigo_pedido not in dicionario_produtos.keys():
        continue

    quantidade = int(input("Digite a Quantaidade: "))

    # calculo do produto e valor.
    produto = dicionario_produtos[codigo_pedido]['produto']
    valor = dicionario_produtos[codigo_pedido]['valor']
    if produto in dicionario_pedido.keys():
        dicionario_pedido[produto]['quantidade'] += quantidade
    else:
        dicionario_pedido[produto] = {"quantidade": quantidade, "valor": valor, "codigo": codigo_pedido}


# sainda final e soma dos produtos.
print("""+------+-----------------+------------+---------------+
| Item | Especificação   | Quantidade | Vl.Quantidade |
+------+-----------------+------------+---------------+
""", end="")
# Calculo do Pedito.
for chave in dicionario_pedido:
    quantidade, valor, codigo = dicionario_pedido[chave].values()
    vl_qunatidade = quantidade * valor
    valor_paga += vl_qunatidade
    item = 0
    print(f"|{codigo:^6}|{chave:<17}|{quantidade:^12}|{vl_qunatidade:>15.2f}|")

print(f"""+------+-----------------+------------+---------------+
| {'Total a pagar':<41} R$ {valor_paga:>7.2f}|
+-----------------------------------------------------+""")
