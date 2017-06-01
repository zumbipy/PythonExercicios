# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaDeDecisao
# Para execurta o programa on line entra no link a baixo:
# https://repl.it/I2Mv/0
"""
16 - Faça um programa que calcule as raízes de uma equação do segundo
grau, na forma ax2 + bx + c. O programa deverá pedir os valores
de a, b e c e fazer as consistências, informando ao usuário nas
seguintes situações:

Se o usuário informar o valor de A igual a zero,
a equação não é do segundo grau e o programa não
deve pedir os demais valores, sendo encerrado;

Se o delta calculado for negativo, a equação não possui
raizes reais. Informe ao usuário e encerre o programa;

Se o delta calculado for igual a zero a equação possui
apenas uma raiz real; informe-a ao usuário;

Se o delta for positivo, a equação possui duas raiz reais;
informe-as ao usuário;
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
a = int(input("Digite o A: "))
b = ""
c = ""

# ================================================================================
#                           Logica do programa
# ================================================================================
# se a igual a zero finaliza programa.
if a == 0:
    print("A igual a 0 então não é uma equação de segundo grau")
else:
    b = int(input("Digite o B: "))
    c = int(input("Digite o C: "))

    # Calculos
    # pra acha a raiz quadrada você pega o valor e divivi por 0.5
    delta = (b**2) - (4 * a * c)
    x2 = (-b + (delta ** 0.5)) / (2 * a)
    x1 = (-b - (delta ** 0.5)) / (2 * a)

    if delta < 0:
        print("o delta calculado é negativo, a equação não possui raizes reais")
    elif delta == 0:
        print(int(x1))
    else:
        print(int(x1))
        print(int(x2))
