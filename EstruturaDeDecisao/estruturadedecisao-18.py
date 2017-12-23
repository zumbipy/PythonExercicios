# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
18 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine
se a mesma é uma data válida.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
data = input("Digite uma data dd/mm/aaaa: ")
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:])
final = ""

# ================================================================================
#                           Logica do programa
# ================================================================================
if dia <= 31 and dia > 0:
    final = "Dia esta OK\n"
else:
    final = "Dia Invalido\n"

if mes <= 12 and mes > 0:
    final += "Mes esta OK\n"
else:
    final += "Mes Invalido\n"

if ano <= 9999 and ano > 0:
    final += "Ano esta OK"
else:
    final += "Ano Invalido"

print("{}/{}/{}".format(dia, mes, ano))
print(final)
