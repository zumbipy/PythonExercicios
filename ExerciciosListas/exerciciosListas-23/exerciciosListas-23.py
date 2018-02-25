# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 23/02/2018
"""
23 - A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco
no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede
precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior
espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte
arquivo, chamado "usuarios.txt":
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar
um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam
necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco,
de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo
programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função,
que será chamada pelo programa principal.
"""


def abrir_arquivo(nome_arquivo):
    with open(nome_arquivo, encoding='UTF-8') as texto:
        return texto.read()


def byte_to_mb(byte):
    mb = byte / 1048576
    return mb


def texto_lista(texto):
    lista_texto = texto.split()
    lista_saida = []
    index = 0
    for loop in range(len(lista_texto) // 2):
        nome = lista_texto[index]
        mb = lista_texto[index + 1]
        lista_saida.append([nome, int(mb)])
        index += 2
    return lista_saida


def percentual(lista_nome_espaco):
    lista_porcentagem = []
    total_espaco = sum([espaco for _, espaco in lista_nome_espaco])
    for nome, espaco in lista_nome_espaco:
        porcentagem = (100 * espaco) / total_espaco
        lista_porcentagem.append(porcentagem)
    return lista_porcentagem


if __name__ == '__main__':
    texto = abrir_arquivo("usuarios.txt")
    lista_nome_espaco = texto_lista(texto)
    lista_porcentagem = percentual(lista_nome_espaco)

    with open("relatório.txt", "w") as saida:

        saida.write("""ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

""")
        ordem = 1
        for (nome, espaco), porcentagem in zip(lista_nome_espaco, lista_porcentagem):
            saida.write(f"{ordem}    {nome:<10}     {byte_to_mb(espaco):>7.2f} MB             {porcentagem:>3.1f}%\n")
            ordem += 1
        total_mb = byte_to_mb(sum([espaco for _, espaco in lista_nome_espaco]))
        media = total_mb / len(lista_nome_espaco)
        saida.write(f"""
Espaço total ocupado: {total_mb:.2f} MB
Espaço médio ocupado: {media:.2f} MB""")
