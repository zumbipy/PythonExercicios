# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/ /dev - 05/02/2018

"""
    Entra em cada diretorio e conta quantos arquivos tem e atulizar o READEME.md
"""

import os


def escrever_arquivo(nome_arquivo, texto):
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(texto)


def dicionaro_de_diretorios(lista_ignora):
    lista_diretorio = os.listdir()
    dic_diretorio = {}
    for diretorio in lista_diretorio:
        if os.path.isdir(diretorio) and diretorio not in lista_ignora:
            dic_diretorio[diretorio] = {'completos': 0}
    return dic_diretorio


def contar_arquivos(dicionario):
    for chave in dicionario.keys():
        total = len(os.listdir(chave))
        dicionario[chave]['completos'] = total


def nomeclatura_diretorio(dicionario):
    nomes_arruma = dicionario.keys()
    saida = ''
    for nome in nomes_arruma:
        for letra in nome:
            if ord(letra) >= 65 and ord(letra) <= 90:
                saida += f" {letra}"
            else:
                saida += letra
        dicionario[nome]['Nome'] = saida.lstrip()
        saida = ''


if __name__ == '__main__':
    lista_ignora = [".git"]
    diretorios = dicionaro_de_diretorios(lista_ignora)
    nomeclatura_diretorio(diretorios)
    contar_arquivos(diretorios)

    texto = """# **Python Exercícios**
> Treinando Algoritmo e Lógica de Programação com os exercícios disponíveis em: https://wiki.python.org.br/ListaDeExercicios

# Lista de exercícios:

 Tipo de exercício | Concluido
----------------------------|:----------------:
"""
    for linha in diretorios.keys():
        Nome_d = diretorios[linha]["Nome"]
        finalizados = diretorios[linha]["completos"]
        texto += f"**{Nome_d}** | {finalizados}\n"

    escrever_arquivo("README.md", texto)
