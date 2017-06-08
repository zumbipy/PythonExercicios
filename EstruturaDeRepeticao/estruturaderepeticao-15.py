# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaDeRepeticaoS
"""
15 - A série de Fibonacci é formada pela seqüência
1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a
série até o n−ésimo termo.
"""
# ================================================================================
#                                      Variaveis.
# ================================================================================
a = 1
b = 0
n_esimo = int(input("Digite o n-ésmo termo: "))

# ================================================================================
#                                   Logica.
# ================================================================================
for i in range(n_esimo):
    c = a + b
    # aqui servi pra coloca '.' no ultimo termo.
    if (n_esimo - 1) > i:
        print("{}, ".format(c), end="")
    else:
        print("{}.".format(c))
    a, b = b, c
