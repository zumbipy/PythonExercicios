# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
'''
    Este aquivo ler os nomes das pastas do diretorio Raiz onde esta e criar um aqruivo com
o NomeDapasta e TotaldeArquivos dentro dela.

'''

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


def file_count(path_dir, type_filer):
    '''Conta o total de arquivos de um tipo especifico.'''

    count = 0
    for ffile in os.listdir(path_dir):
        if ffile.endswith(type_filer):
            count += 1
    return count


def upper_one(wold):
    '''Analiza uma palavra e coloca espaço antes de cada letra Miuscula.'''

    UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_wold = ''
    for letter in wold:
        if letter in UPPER:
            new_wold += ' '
        new_wold += letter
    return new_wold


def list_for_table(llist_dir, dict_num=dict()):
    '''Recebe 2 paramento 'llist_dir' uma lista de nome de pastas e o 'dict_num' 
    um dict() onde chave e um numero e o valor total de arquivo pra fazer. '''

    table_html = ''
    for key, diretorio in enumerate(llist_dir):
        table_html += f'''
<tr>
    <td>{upper_one(diretorio)}</td>
    <td>{file_count(diretorio, ".py")} | {dict_num.get(key, '???')}</td> 
</tr>
        '''
    return table_html


def render(file_out, base, context):
    '''Recebe 3 paramentros é gera um arquivo.
    file_out = nome do aquivo de saida.
    base = Um arquivo com a palavra "CODE" dentro, onde vai se subtituido por outro conteúdo.
    context = Uma string pra se colocanda dentro do aquivo base para depois se salvo como file_out.'''


    with open(base, 'r', encoding='utf-8') as f:
        html = f.read()

    with open(file_out, 'w', encoding='utf-8') as f:
        f.write(html.replace('CODE', context))


if __name__ == '__main__':
    dicionario = {
        0 : 28,
        1 : 51,
        2 : 18,
        3 : 17,
        4 : 13,
        5 : 24,
    }
    context = list_for_table(list_dir('.'), dicionario)
    render('README.md', 'template.html', context)
