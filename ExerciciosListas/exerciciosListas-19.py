# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 17/02/2018
"""
19 - Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande
quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final
o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a
entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6).
Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem
sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes
e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
"""


def criar_enquete(pergunta, lista_opcoes):
    print(f"{pergunta}\n")
    print("As possíveis respostas são:\n")
    for _, titulo, codigo in lista_opcoes:
        print(f"{codigo}- {titulo}")
    print()


def criar_lista(lista_nomes):
    ''' Recebe uma lista de nome é retorna uma lista com [[voto, nome, codigo], ...]
    sendo votos igual a 0'''

    lista_saida = []
    for ordem, nome in enumerate(lista_nomes):
        lista_saida.append([0, nome, ordem + 1])
    return lista_saida


def opcao_votar(lista_opcoes):
    lista_vota = [x[2] for x in lista_opcoes]
    return lista_vota


def validar_votos(voto, lista_opcoes):
    if voto in opcao_votar(lista_opcoes):
        return True
    else:
        print("Valor Invalido!!!")
        return False


def total_votos(lista_opcoes):
    return sum([x[0] for x in lista_opcoes])


def porcentage(lista_opcoes):
    t_votos = total_votos(lista_opcoes)
    lista_porcentage = []
    for voto, titulo, codigo in lista_opcoes:
        try:
            porcentage = (100 * voto) / t_votos
            lista_porcentage.append([voto, titulo, codigo, porcentage])
        except Exception as e:
            pass
    return lista_porcentage


def imprimir_resultado(lista_opcoes):
    print(f'''Sistema Operacional     Votos   %
-------------------     -----   ---''')
    for voto, titulo, codigo, porcentage in lista_opcoes:
        print(f'{titulo:<25}{voto:<6.0f}{porcentage:>3.0f}%')
    if lista_opcoes:
        voto, titulo, codigo, porcentage = max(lista_opcoes)
    else:
        voto, titulo, codigo, porcentage = 0, 0, 0, 0
    print(f'''-------------------     -----
Total                    {total_votos(lista_opcoes):<7.0f}

O Sistema Operacional mais votado foi o {titulo}, com {voto} votos, correspondendo a {porcentage:.0f}% dos votos.''')


if __name__ == '__main__':

    pergunta = "Qual o melhor Sistema Operacional para uso em servidores?"
    lista_opcoes = criar_lista(('Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro'))
    criar_enquete(pergunta, lista_opcoes)

    while True:
        try:
            vota = int(input("Digite o codigo que deseja vota: "))
        except Exception as e:
            print("Codigo Invalido!!!")
            continue
        if vota == 0:
            print()
            break
        if validar_votos(vota, lista_opcoes):
            lista_opcoes[vota - 1][0] += 1

    lista_opcoes = porcentage(lista_opcoes)
    imprimir_resultado(lista_opcoes)
