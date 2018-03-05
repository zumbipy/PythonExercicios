# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 04/03/2018
"""
06 - Faça um programa que use a função valorPagamento para determinar o
valor a ser pago por uma prestação de uma conta. O programa deverá solicitar
ao usuário o valor da prestação e o número de dias em atraso e passar estes
valores para a função valorPagamento, que calculará o valor a ser pago e
devolverá este valor ao programa que a chamou. O programa deverá então exibir
o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir
outro valor de prestação e assim continuar até que seja informado um valor igual
a zero para a prestação. Neste momento o programa deverá ser encerrado,
exibindo o relatório do dia, que conterá a quantidade e o valor total
de prestações pagas no dia. O cálculo do valor a ser pago é feito da
seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação.
Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
"""


def valor_pagamento(valor, dias=0):
    if dias:
        multa = valor * 0.03
        juros = (valor * 0.001) * dias
        return valor + multa + juros
    else:
        return valor


def main():
    quantidade_prestacao_dia = 0
    valor_total_prestacao_dia = 0
    while True:
        valor_prestacao = float(input("Digite o valor da prestação: "))

        if valor_prestacao:
            dias_atraso = int(input("Digite total de dias em atraso: "))
            valor_pagar = valor_pagamento(valor_prestacao, dias_atraso)
            print(f"Valor total a pagar: R$ {valor_pagar:.2f}\n")

            quantidade_prestacao_dia += 1
            valor_total_prestacao_dia += valor_pagar
        else:
            break
    print(f"Relatório do dia: {quantidade_prestacao_dia} prestações pagas com o valor total de R$ {valor_total_prestacao_dia} reais.")


if __name__ == '__main__':
    main()