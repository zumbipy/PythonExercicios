# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 26/02/2018
"""
05 - Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros.
Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre
a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para
efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um
loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as
vezes que desejar.
"""


def converte_horario(hora, minuto):
    hora, minuto = f"{hora:0>2}", str(minuto)
    horas_24 = ['13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '00']
    horas_12 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    modo = "a"
    if hora in horas_24:
        hora = horas_12[horas_24.index(hora)]
        modo = "p"
        return hora, minuto, modo
    else:
        return hora, minuto, modo


def saida(hora, minuto, modo):
    modo = "P.M" if modo == "p" else "A.M"
    print(f"{hora}:{minuto} {modo}")


if __name__ == '__main__':
    while True:
        hora = int(input("Digte as horas: "))
        minuto = int(input("Digte as minutos: "))
        hora, minuto, modo = converte_horario(hora, minuto)
        saida(hora, minuto, modo)
        print()
