# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaDeDecisao
# Para execurta o programa on line entra no link a baixo:
# https://repl.it/I2Ee/0
"""
13 - Faça um Programa que leia um número e exiba o dia correspondente
da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor
deve aparecer valor inválido.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
# Entrada de Dados.
dia_da_semana = int(input("Digite Um numero de 1 ao 7: "))

# ================================================================================
#                           Logica do programa
# ================================================================================
# Comparações.
if dia_da_semana == 1:
    print("Numero {} correspondente á Domingo".format(dia_da_semana))

elif dia_da_semana == 2:
    print("Numero {} correspondente á Segunda".format(dia_da_semana))

elif dia_da_semana == 3:
    print("Numero {} correspondente á Terça".format(dia_da_semana))

elif dia_da_semana == 4:
    print("Numero {} correspondente á Quarta".format(dia_da_semana))

elif dia_da_semana == 5:
    print("Numero {} correspondente á Quinta".format(dia_da_semana))

elif dia_da_semana == 6:
    print("Numero {} correspondente á Sexta".format(dia_da_semana))

elif dia_da_semana == 7:
    print("Numero {} correspondente á Sabado".format(dia_da_semana))

else:
    print("Valor Invalido.")
