# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/

import os
import os.path


def list_dir(path_dir, hidden_file='.'):
    '''Pega um caminho de arquivo é retorna uma lista só com os nomes
    de diretorios.'''

    list_name = []
    for name in os.listdir(path_dir):
        if name.startswith(hidden_file):
            continue
        else:
            if os.path.isdir(name):
                list_name.append(name)
    return list_name


def file_counter(path_dir, type_filer):
    '''Conta o total de arquivos de um tipo especifico.'''

    count = 0
    for ffile in os.listdir(path_dir):
        if ffile.endswith(type_filer):
            count += 1
    return count


def upper_one(wold):
    '''Analiza uma palavra e coloca espaço antes de cada letra Maiuscula.'''

    UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_wold = ''
    for letter in wold:
        if letter in UPPER:
            new_wold += ' '
        new_wold += letter
    return new_wold


for diretorio in list_dir('.'):
    print(f'{upper_one(diretorio)} | {file_counter(diretorio, ".py")}|')
