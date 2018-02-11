# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 09/02/2018
"""
46 - Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados.
O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um
programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e
depois informe a média dos saltos conforme a descrição acima informada
(retirar o melhor e o pior salto e depois calcular a média).
Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução,
portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta.
A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
6.5, 6.1, 6.2, 5.4, 5.3
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m
"""


def salto():
    lista = []
    for salto in range(5):
        distancia = float(input(f"Digite o salto {salto + 1}/5: "))
        lista.append(distancia)
    return lista


def media_salto(lista):
    lista_media = lista.copy()
    lista_media.sort()
    media = sum(lista_media[1:4]) / 3
    return round(media, 2)


def maior_menor(lista):
    maior, menor = max(lista), min(lista)
    return maior, menor


def vizualizar_lista(lista):
    for item in lista:
        if item != lista[-1]:
            print(f"{item}, ", end='')
        else:
            print(f"{item}")


def vizualizar_resultados(lista):
    ordem_pulos = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']

    for atleta in lista:
        nome, saltos, _, media = atleta
        maior, menor = _

        print(f"""Atleta: {nome}""")
        vizualizar_lista(saltos)

        for ordem, salto in zip(ordem_pulos, saltos):
            print(f'{ordem} Salto: {salto:.1f} m')

        print(f"""
Melhor salto:  {maior:.1f} m
Pior salto: {menor:.1f} m
Média dos demais saltos: {media:.1f} m

Resultado final:
{nome}: {media:.1f} m
""")


if __name__ == "__main__":
    lista_atletas = []

    while True:
        nome = input("Qual seu Nome: ")
        if nome == '':
            print()
            break
        lista_saltos = salto()
        media = media_salto(lista_saltos)
        maior, menor = maior_menor(lista_saltos)
        lista_atletas.append([nome, lista_saltos, [maior, menor], media])

    vizualizar_resultados(lista_atletas)
