# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 22/02/2018
"""
22 - Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática,
com a intenção de fazer um levantamento nas sucatas encontradas nesta área.
A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e
anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
    Foi requisitado que você desenvolva um programa para registrar este levantamento.
    O programa deverá receber um número indeterminado de entradas, cada uma contendo:
    um número de identificação do mouse o tipo de defeito:
    necessita da esfera;
    necessita de limpeza;
    a.necessita troca do cabo ou conector;
    a.quebrado ou inutilizado.
    Uma identificação igual a zero encerra o programa.
    Ao final o programa deverá emitir o seguinte relatório:

Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
"""


def porcentural(lista_defeitos):
    total_equipamento = len(lista_equipamento)
    lista_porcentagem = []
    for defeito in lista_defeitos:
        if defeito == 0:
            porcentagem = 0
        else:
            porcentagem = (100 * defeito) / total_equipamento
        lista_porcentagem.append(porcentagem)
    return lista_porcentagem


def quantidade_tipo_defeitos(lista_equipamento):
    lista_defeitos = [0, 0, 0, 0]
    for _, defeito in lista_equipamento:
        if defeito == 1:
            lista_defeitos[0] += 1
        elif defeito == 2:
            lista_defeitos[1] += 1
        elif defeito == 3:
            lista_defeitos[2] += 1
        else:
            lista_defeitos[3] += 1
    return lista_defeitos


if __name__ == '__main__':
    lista_equipamento = []
    lista_porcentagem = []
    lista_defeitos = []

    while True:
        id_equipamento = int(input("Digite a id do equipamento: "))

        if id_equipamento == 0:
            break

        print("""1 - necessita da esfera.
2 - necessita de limpeza.
3 - necessita troca do cabo ou conector.
4 - quebrado ou inutilizado.""")

        while True:
            tipo_defeito = int(input("Digite o codigo do erro de 1 ao 4: "))
            if tipo_defeito in [1, 2, 3, 4]:
                break
            else:
                print("Valor Invalido!!!")

        lista_equipamento.append([id_equipamento, tipo_defeito])
        print()

    lista_defeitos = quantidade_tipo_defeitos(lista_equipamento)
    lista_porcentagem = porcentural(lista_defeitos)
    total_equipamentos = len(lista_equipamento)

    print(f"""\nQuantidade de mouses: {total_equipamentos}

Situação                         Quantidade              Percentual
1- necessita da esfera                  {lista_defeitos[0]:0>3}                     {lista_porcentagem[0]:0>2.0f}%
2- necessita de limpeza                 {lista_defeitos[1]:0>3}                     {lista_porcentagem[1]:0>2.0f}%
3- necessita troca do cabo ou conector  {lista_defeitos[2]:0>3}                     {lista_porcentagem[2]:0>2.0f}%
4- quebrado ou inutilizado              {lista_defeitos[3]:0>3}                     {lista_porcentagem[3]:0>2.0f}%
""")
