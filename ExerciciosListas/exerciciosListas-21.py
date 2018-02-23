# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 21/02/2018
"""
21 - Faça um programa que carregue uma lista com os modelos de cinco carros
(exemplo de modelos: FUSCA, GOL, VECTRA etc).
Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um
litro de combustível. Calcule e mostre:
O modelo do carro mais econômico;
Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros
e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo.
O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a
cada execução do programa.
Comparativo de Consumo de Combustível

Veículo 1
Nome: fusca
Km por litro: 7
Veículo 2
Nome: gol
Km por litro: 10
Veículo 3
Nome: uno
Km por litro: 12.5
Veículo 4
Nome: Vectra
Km por litro: 9
Veículo 5
Nome: Peugeout
Km por litro: 14.5

Relatório Final
 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
O menor consumo é do peugeout.
"""


def consumo_gasolina(lista_veiculos):
    lista_consumo = []
    for _, litros in lista_veiculos:
        lista_consumo.append(1000 / litros)
    return lista_consumo


def valor_gasolina(lista_consumo, valor_litro):
    total_pago = []
    for litro in lista_consumo:
        total_pago.append(litro * valor_litro)
    return total_pago


def menor_cosumo(lista_consumo):
    menor = min(lista_consumo)
    return lista_consumo.index(menor)


def imprimir_relatorio(lista_veiculos):
    lista_consumo = consumo_gasolina(lista_veiculos)
    valor_total = valor_gasolina(lista_consumo, 2.25)
    consumo = consumo_gasolina(lista_veiculos)
    print("Relatório Final")
    posicao = 1
    for (nome, litros), consumo, valor in zip(lista_veiculos, consumo, valor_total):
        print(f"{posicao} - {nome.lower()}           -    {litros:>.1f} -  {consumo:.1f} litros - R$ {valor:.2f}")
        posicao += 1

    menor = menor_cosumo(lista_consumo)
    print(f"O menor consumo é do {lista_veiculos[menor][0]}.")


if __name__ == '__main__':
    lista_veiculos = []

    for repetir in range(5):
        print(f"Veículo {repetir + 1}")
        nome = input("Nome: ")
        litro_km = float(input('Km por litro: '))
        lista_veiculos.append([nome, litro_km])
    imprimir_relatorio(lista_veiculos)
