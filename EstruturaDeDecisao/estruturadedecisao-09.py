# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
9 - Faça um Programa que leia três números e
mostre-os em ordem decrescente.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
# Entrada de Dados.
a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))

# ================================================================================
#                           Logica do programa
# ================================================================================
"""
    A logica e a mesmo dos outros 3, o que mudou foi o metodo que uso pra
marca as saida.
    Colocando um variavel dento do {} e so mudado a atribuição a cada print.
"""
if a >= b >= c:
    print("{na},{nb} ,{nc} ".format(na=a, nb=b, nc=c))

elif a >= b <= c <= a:
    print("{na}, {nb}, {nc}".format(na=a, nb=c, nc=b))

elif a <= b >= c <= a:
    print("{na}, {nb}, {nc}".format(na=b, nb=a, nc=c))

elif a >= b <= c >= a:
    print("{na}, {nb}, {nc}".format(na=c, nb=a, nc=b))

elif a <= b >= c <= b:
    print("{na}, {nb}, {nc}".format(na=b, nb=c, nc=a))

elif a <= b <= c:
    print("{na}, {nb}, {nc}".format(na=c, nb=b, nc=a))
