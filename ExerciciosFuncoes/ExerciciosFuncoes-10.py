# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/ /dev 07/02/2018
"""
10 - Data com mês por extenso.
Construa uma função que receba uma data no formato DD/MM/AAAA
e devolva uma string no formato D de mesPorExtenso de AAAA.
Opcionalmente, valide a data e retorne NULL caso a data
seja inválida.
"""


def mes_por_externso(entrada_mes):
    dict_mes = {
        '01': 'Janeiro',
        '02': 'Fevereiro',
        '03': 'Março',
        '04': 'Abril',
        '05': 'Maio',
        '06': 'Junho',
        '07': 'Julho',
        '08': 'Agosto',
        '09': 'Setembro',
        '10': 'Outubro',
        '11': 'Novembro',
        '12': 'Dezembro',
    }
    dia, mes, ano = entrada_mes.split("/")
    print(f"{dia} de {dict_mes[mes]} de {ano}")


def valida_data(entrada_data):
    if entrada_data.count("/") != 2:
        return False

    dia, mes, ano = entrada_data.split("/")
    lista_dia = [str(x) for x in range(1, 32)]
    lista_mes = [str(x) for x in range(1, 13)]
    lista_ano = [str(x) for x in range(1000, 10000)]

    if dia not in lista_dia:
        return False
    if mes not in lista_mes:
        return False
    if ano in lista_ano:
        return True
    return True


def main():
    print(valida_data("12/12/1222"))
    data = input("Digite uma data no formato DD/MM/AAAA: ")
    if valida_data(data):
        mes_por_externso(data)
    else:
        print("NULL")


if __name__ == '__main__':
    main()
