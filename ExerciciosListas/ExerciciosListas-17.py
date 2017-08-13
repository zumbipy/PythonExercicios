# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaLista
"""
17 -Em uma competição de salto em distância cada atleta tem direito a
cinco saltos. O resultado do atleta será determinado pela média dos
cinco valores restantes. Você deve fazer um programa que receba o nome
e as cinco distâncias alcançadas pelo atleta em seus saltos e depois
informe o nome, os saltos e a média dos saltos. O programa deve ser
encerrado quando não for informado o nome do atleta. A saída do programa
deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""

lista_atleta = []
lista_P = ["Primeiro Salto: ", "Segundo Salto: ", "Terceiro Salto: ",
           "Quarto Salto: ", "Quinto Salto: "]
nome_atleta = None
soma_saltos = 0
saltos = 0
media_saltos = soma_saltos / 5

while True:
    nome_atleta = input("Nome do Atleta ou aperte entre pra sair: ")
    lista_atleta.append(nome_atleta)
    print()

    # Condição de parada.
    if nome_atleta == "":
        break

    # Loop de perguntas de 1 ao 5.
    for r in range(5):
        saltos = float(input("{}".format(lista_P[r])))
        lista_atleta.append(saltos)
        soma_saltos += saltos
    print()
    media_saltos = soma_saltos / 5
    lista_atleta.append(media_saltos)

    print("Resultado final:")
    print("Atleta: {[0]}".format(lista_atleta))
    print("Saltos: {0[1]:.1f} - {0[2]:.1f} - {0[3]:.1f} - {0[4]:.1f} - {0[5]:.1f}".format(lista_atleta))
    print("Média dos saltos: {[6]:.1f} m".format(lista_atleta))
    print()

    # Reset as variaveis.
    media_saltos = 0
    soma_saltos = 0
    saltos = 0
    lista_atleta = []
