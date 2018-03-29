# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/ /dev - 05/02/2018

"""
    Entra em cada diretorio e conta quantos arquivos tem e atulizar o READEME.md
"""
import os
import os.path
from string import ascii_uppercase


def criar_ler_arquivo(nome_arquivo, texto="", tipo="w"):
    'criar_ler_arquivo(arquivo, texto="", tipo="")'

    if tipo == "w":
        with open(nome_arquivo, tipo, encoding="utf-8") as arquivo:
            arquivo.write(texto)
    elif tipo == "r":
        with open(nome_arquivo, tipo, encoding="utf-8") as arquivo:
            return arquivo.read()


def criar_dict_diretorio():

    dict_diretorios = {diretorio: {} for diretorio in os.listdir() if os.path.isdir(diretorio)
                       if "." not in diretorio}

    for diretorio in dict_diretorios.keys():
        dict_diretorios[diretorio]["Nome"] = separa_nome(diretorio)
        dict_diretorios[diretorio]["Total"] = conta_arquivos(diretorio, ["py"])

    return dict_diretorios


def separa_nome(palavra):
    saida = ''
    for letra in palavra:
        if letra in ascii_uppercase:
            saida += " " + letra
        else:
            saida += letra
    return saida.lstrip()


def conta_arquivos(local, tipos=["py"]):
    total = 0
    for arquivo in os.listdir(local):
        if arquivo.split(".")[1] in tipos:
            total += 1
    return total


def template_texto(texto, dict_diretorios):
    saida = texto
    for chave in dict_diretorios:
        saida += f'**{dict_diretorios[chave]["Nome"]}** | **{dict_diretorios[chave]["Total"]} \ {dict_diretorios[chave].get("Falta", 0)}**\n'
    return saida


def mesclar_dic(dic, dict_juntar):
    for chave in dict_juntar:
        if chave in dic.keys():
            dic[chave].update(dict_juntar[chave])


def commit():
    '''So fucionar se não perdir senha ou login eo mesmo tive cido modificado'''
    os.system("git add README.md")
    os.system("git commit -m 'Update'")
    os.system("git push")


if __name__ == '__main__':
    dict_juntar = {'EstruturaDeDecisao': {"Falta": 28},
                   'EstruturaDeRepeticao': {"Falta": 51},
                   'EstruturaSequencial': {"Falta": 18},
                   "ExerciciosClasses": {"Falta": 17},
                   'ExerciciosListas': {"Falta": 24},
                   'ExerciciosFuncoes': {"Falta": 13},
                   }

    texto = criar_ler_arquivo("texto_readema.txt", tipo="r")
    dic = criar_dict_diretorio()
    mesclar_dic(dic, dict_juntar)
    criar_ler_arquivo("README.md", template_texto(texto, dic))
    print(criar_ler_arquivo("README.md", tipo="r"))
    commit()
