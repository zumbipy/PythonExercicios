# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
31 - O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios
de 1,99 e agora possui uma loja de conveniências. Faça um programa que
implemente uma caixa registradora rudimentar. O programa deverá receber
um número desconhecido de valores referentes aos preços das mercadorias.
Um valor zero deve ser informado pelo operador para indicar o final da compra.
O programa deve então mostrar o total da compra e perguntar o valor em
dinheiro que o cliente forneceu, para então calcular e mostrar o valor
do troco. Após esta operação, o programa deverá voltar ao ponto inicial,
para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
...
"""
while True:
    produto_valor = 0
    valor_total = 0
    troco = 0
    contador_produto = 0
    pagamento = 0
    print("Lojas Tabajara\nDigitre 0 para finalizar!\n")
    while True:
        contador_produto += 1
        produto_valor = float(input("Produto{:>2}: R$ ".format(
            contador_produto)))

        if produto_valor == 0:
            break
        else:
            valor_total += produto_valor

    print("Total :    R$ {:.2f}".format(valor_total))
    pagamento = float(input("Dinheiro:  R$ "))
    troco = pagamento - valor_total
    print("Troco:     R$ {:.2f}".format(troco))
    print("{:=^40}".format(""))
