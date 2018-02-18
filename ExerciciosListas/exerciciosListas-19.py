# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 17/02/2018
"""
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande
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


def enquete(pergunta, lista_opcoes):
    print(f"{pergunta}\n")
    print("As possíveis respostas são:\n")
    for ordem, opcao in enumerate(lista_opcoes):
        print(f"{ordem + 1}- {opcao}")


def validar_voto(voto, lista_opcoes):
    voto = int(voto)
    opcaoes = convert_lista_numeros(lista_opcoes)
    return True if voto in opcaoes else False


def conta_votos(lista_votos, lista_opcoes):
    lista_votos.sort()
    numeros = convert_lista_numeros(lista_opcoes)
    return [lista_votos.count(x) for x in numeros]


def convert_lista_numeros(lista):
    lista_numero = [x + 1 for x in range(len(lista))]
    return lista_numero


def percentual(lista_votos):
    lista_porcetual = []
    total_votos = sum(lista_votos)
    for voto in lista_votos:
        porcetual = (100 * voto) / total_votos
        lista_porcetual.append([voto, porcetual])
    return lista_porcetual


def imprimir_resultado(lista_porcetual, lista_opcoes, total_votos):
    print(f'''Sistema Operacional     Votos   %
-------------------     -----   ---''')
    for (votos, porcetual), OS in zip(lista_porcetual, lista_opcoes):
        print(f'{OS:<25}{votos:<6.0f}{porcetual:>3.0f}%')
    lista_porcetual.sort()
    print(f'''-------------------     -----
Total                    {total_votos:<7.0f}


O Sistema Operacional mais votado tem {lista_porcetual[-1][0]} votos, correspondendo a {lista_porcetual[-1][1]:.0f}% dos voto''')


if __name__ == '__main__':

    pergunta = "Qual o melhor Sistema Operacional para uso em servidores?"
    lista_opcoes = ('Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro')
    lista_votos = []

    enquete(pergunta, lista_opcoes)
    while True:
        try:
            voto = int(input("Digite o numero do OS que deseja vota: "))
        except Exception as erro:
            print("Digite apenas valores inteiros positivos")
            continue

        if voto == 0:
            break
        if validar_voto(voto, lista_opcoes):
            lista_votos.append(voto)
        else:
            print("Valor invalido!!!")

    lista_votos = conta_votos(lista_votos, lista_opcoes)
    total_votos = sum(lista_votos)

    imprimir_resultado(percentual(lista_votos), lista_opcoes, total_votos)
