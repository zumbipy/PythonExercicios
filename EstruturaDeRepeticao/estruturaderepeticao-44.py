# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/ /dev - 04/02/2018
"""
44 - Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de
código.
Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos
tem-se o valor zero.
"""

dic_candidatos = {
    1: {"canditado": "joao", "voto": 0},
    2: {"canditado": "maria", "voto": 0},
    3: {"canditado": "josé", "voto": 0},
    4: {"canditado": "nego ban", "voto": 0},
    5: {"canditado": "Voto Nulo", "voto": 0},
    6: {"canditado": "Voto Branco", "voto": 0}

}


def tabela_eleicao(dic):
    print("""
+-----+------------+-------+
| cod | Candidatos | Votos |
+-----+------------+-------+""")
    for codigo in dic.keys():
        votos = dic[codigo]['voto']
        candidato = dic[codigo]['canditado']
        if codigo == 5:
            print("+-----+------------+-------+")
            print(f"|{codigo:^5}|{candidato.capitalize():<12}|{votos:>7}|")

        else:
            print(f"|{codigo:^5}|{candidato.capitalize():<12}|{votos:>7}|")
    print("+-----+------------+-------+")


def votar(dic):
    while True:
        codigo_voto = int(input("Para voto digite o codigo do Canditado ou 0 para sair: "))
        if codigo_voto in dic.keys():
            dic[codigo_voto]['voto'] += 1
            print("Voto confirmando")
        else:
            print("Codigo Invalido !!! voto não confirmando!!")
        if codigo_voto == 0:
            return False


def contar_votos(dic_candidatos):
    total = 0
    for codigo in dic_candidatos.keys():
        voto = dic_candidatos[codigo]['voto']
        total += voto
    return total


def calcular_porcentagem(dic_candidatos):
    total_votos = contar_votos(dic_candidatos)
    votos_nulos = dic_candidatos[5]['voto']
    votos_brancos = dic_candidatos[6]['voto']

    p_votos_nulos = (100 * votos_nulos) / total_votos
    p_votos_brancos = (100 * votos_brancos) / total_votos
    print(f"Total de Votos foram: {total_votos}")
    print(f"Total de votos brancos foi: {p_votos_brancos:.1f}%")
    print(f"Total de votos nulos foi: {p_votos_nulos:.1f}%")


if __name__ == '__main__':
    tabela_eleicao(dic_candidatos)
    votar(dic_candidatos)
    tabela_eleicao(dic_candidatos)
    calcular_porcentagem(dic_candidatos)
