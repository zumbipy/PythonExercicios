# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaDeDecisao
# Para execurta o programa on line entra no link a baixo:
# https://repl.it/I29b/0
"""
28 - O Hipermercado Tabajara está com uma promoção de carnes que é imperdível.

Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

    Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos
de carne da promoção, porém não há limites para a quantidade de carne por
cliente.
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto
de 5% sobre o total da compra.
    Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário
e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne,
preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""
# ================================================================================
#                           Tabela de Preço
# ================================================================================
print("""
+======================================================+
|                   Tabeça de Preços                   |
+======================================================+
|                      Até 5 Kg           Acima de 5 Kg|
|File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg|
|Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg|
|Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg|
+======================================================+
|   Se pagar no Cartão Tabajara ganhar 5% desconto.    |
+======================================================+""")

# Entrada de dados com 3 opções e usando .lower() nos textos.
tipo_de_carne = input("""Qual tipo de carne:
File Duplo (F)
Alcatra    (A)
Picanha    (P)
Digite a opção desejada: """).lower()
peso_carne = int(input("Vai compra quantos Kilos de Carne?: "))
tipo_pagamento = input("Vai Pagar no Cartao(C) ou Dinheiro(D)?: ").lower()

# Comparação e atribuição dos valores promocionais.
file_duplo = 4.90 if peso_carne <= 5 else 5.80
alcatra = 5.90 if peso_carne <= 5 else 6.80
picanha = 6.90 if peso_carne <= 5 else 7.80
desconto = 0

# ================================================================================
#                           Logica do programa
# ================================================================================
# Verifica se é cartao.
if "cartao".startswith(tipo_pagamento):
    # Subtituir o valor pra um novo.
    tipo_pagamento = "Cartao Tabajara"

    # Verefica o tipo de carne se for F.
    if "file duplo".startswith(tipo_de_carne):
        # Subtituir o valor pra um novo.
        tipo_de_carne = "File Duplo"
        valor_da_compra = peso_carne * file_duplo
        desconto = valor_da_compra * 0.05
        valor_total = valor_da_compra - desconto

        # Sainda do Programa.
        print("""
    +=============================================+
    |               CUPOM FISCAL                  |
    +=============================================+
    |Tipo de Carne          |    {:<17}|
    |Tipo de pagamento      |    {:<17}|
    |Quantidade de carne Kg |    {:<17.2f}|
    |Preço Da compra     R$ |    {:<17.2f}|
    |Valor do desconto   R$ |    {:<17.2f}|
    +=============================================+
    |Preço total            |R$: {:<17.2f}|
    +=============================================+
    """.format(tipo_de_carne, tipo_pagamento, peso_carne, valor_da_compra,
               desconto, valor_total))

    elif "alcatra".startswith(tipo_de_carne):
        tipo_de_carne = "Alcatra"
        valor_da_compra = peso_carne * alcatra
        desconto = valor_da_compra * 0.05
        valor_total = valor_da_compra - desconto
        print("""
    +=============================================+
    |               CUPOM FISCAL                  |
    +=============================================+
    |Tipo de Carne          |    {:<17}|
    |Tipo de pagamento      |    {:<17}|
    |Quantidade de carne Kg |    {:<17.2f}|
    |Preço Da compra     R$ |    {:<17.2f}|
    |Valor do desconto   R$ |    {:<17.2f}|
    +=============================================+
    |Preço total            |R$: {:<17.2f}|
    +=============================================+
    """.format(tipo_de_carne, tipo_pagamento, peso_carne, valor_da_compra,
               desconto, valor_total))

    elif "picanha".startswith(tipo_de_carne):
        tipo_de_carne = "Picanha"
        valor_da_compra = peso_carne * picanha
        desconto = valor_da_compra * 0.05
        valor_total = valor_da_compra - desconto
        print("""
    +=============================================+
    |               CUPOM FISCAL                  |
    +=============================================+
    |Tipo de Carne          |    {:<17}|
    |Tipo de pagamento      |    {:<17}|
    |Quantidade de carne Kg |    {:<17.2f}|
    |Preço Da compra     R$ |    {:<17.2f}|
    |Valor do desconto   R$ |    {:<17.2f}|
    +=============================================+
    |Preço total            |R$: {:<17.2f}|
    +=============================================+
    """.format(tipo_de_carne, tipo_pagamento, peso_carne, valor_da_compra,
               desconto, valor_total))
else:
    # Aqui começa a parte se não for cartão.
    tipo_pagamento = "Dinheiro"
    if "file duplo".startswith(tipo_de_carne):
        tipo_de_carne = "File Duplo"
        valor_da_compra = peso_carne * file_duplo
        desconto = 0
        valor_total = valor_da_compra
        print("""
    +=============================================+
    |               CUPOM FISCAL                  |
    +=============================================+
    |Tipo de Carne          |    {:<17}|
    |Tipo de pagamento      |    {:<17}|
    |Quantidade de carne Kg |    {:<17.2f}|
    |Preço Da compra     R$ |    {:<17.2f}|
    |Valor do desconto   R$ |    {:<17.2f}|
    +=============================================+
    |Preço total            |R$: {:<17.2f}|
    +=============================================+
    """.format(tipo_de_carne, tipo_pagamento, peso_carne, valor_da_compra,
               desconto, valor_total))

    elif "alcatra".startswith(tipo_de_carne):
        tipo_de_carne = "Alcatra"
        valor_da_compra = peso_carne * alcatra
        desconto = 0
        valor_total = valor_da_compra
        print("""
    +=============================================+
    |               CUPOM FISCAL                  |
    +=============================================+
    |Tipo de Carne          |    {:<17}|
    |Tipo de pagamento      |    {:<17}|
    |Quantidade de carne Kg |    {:<17.2f}|
    |Preço Da compra     R$ |    {:<17.2f}|
    |Valor do desconto   R$ |    {:<17.2f}|
    +=============================================+
    |Preço total            |R$: {:<17.2f}|
    +=============================================+
    """.format(tipo_de_carne, tipo_pagamento, peso_carne, valor_da_compra,
               desconto, valor_total))

    elif "picanha".startswith(tipo_de_carne):
        tipo_de_carne = "Picanha"
        valor_da_compra = peso_carne * picanha
        desconto = 0
        valor_total = valor_da_compra
        print("""
    +=============================================+
    |               CUPOM FISCAL                  |
    +=============================================+
    |Tipo de Carne          |    {:<17}|
    |Tipo de pagamento      |    {:<17}|
    |Quantidade de carne Kg |    {:<17.2f}|
    |Preço Da compra     R$ |    {:<17.2f}|
    |Valor do desconto   R$ |    {:<17.2f}|
    +=============================================+
    |Preço total            |R$: {:<17.2f}|
    +=============================================+
    """.format(tipo_de_carne, tipo_pagamento, peso_carne, valor_da_compra,
               desconto, valor_total))
