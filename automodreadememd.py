# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __ 
#   / /_/ // /  ' \/ _ \/ / ___/ // / 
#  /___/\_,_/_/_/_/_.__/_/_/   \_, / 
# E-mail: zumbipy@gmail.com   /___/ 

import os, os.path

def list_dir(path_dir):
    list_name=[]
    for name in os.listdir(path_dir):
        print(name)
        if name.startswith('.'):
             continue
        else:
            if os.path.isdir(name):
                list_name.append(name)

    print(list_name)
    return list_name

list_dir('.')