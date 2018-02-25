# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 25/02/2018
"""
17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o
tamanho em metros quadrados da área a ser pintada. Considere que a cobertura
da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga
e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""


def m2_litros(m2):
    m2 += (m2 * 0.1)
    return m2 * 6


def latas_tintas(litros, lata_galao):
    total_latas_galao = round((litros / lata_galao) + 0.)
    return total_latas_galao


def pagar_lata_galao(total_latas_galao, valores):
    return total_latas_galao * valores


def media_lata_galao(litros):
    lata = (litros // 18)
    galao = round(((litros - (lata * 18)) / 3.6) + 0.5)
    return lata, galao


if __name__ == '__main__':
    metros = int(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
    litros = m2_litros(metros)

    lata = latas_tintas(litros, 18)
    galao = latas_tintas(litros, 3.6)
    print(f"Comprando {lata} latas de 18 litros vai pagar R$ {pagar_lata_galao(lata, 80):.2f} e vai sobra {abs(lata * 18 - litros):.0f} litros.")
    print(f"Comprando {galao} galões de 3,6 litros vai pagar R$ {pagar_lata_galao(galao, 25):.2f} e vai sobra {abs(int(galao * 3.6 - litros)):.0f} litros.")
    lata, galao = media_lata_galao(litros)
    total_pagar = lata * 80 + galao * 25
    sobra = litros - (lata * 18 + galao * 3.6)
    print(f"Comprando {int(lata)} latas e {galao} galões vai paga R$ {total_pagar} reais e vai sobra {abs(sobra):.0f} litros")
