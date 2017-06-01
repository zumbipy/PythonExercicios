# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaDeDecisao
# Para execurta o programa on line entra no link a baixo:
# https://repl.it/I0l3/1
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
