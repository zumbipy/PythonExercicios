# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaDeDecisao
# Para execurta o programa on line entra no link a baixo:
# https://repl.it/I22o/0
"""
21 - Faça um Programa para um caixa eletrônico. O programa deverá
perguntar ao usuário a valor do saque e depois informar quantas
notas de cada valor serão fornecidas. As notas disponíveis serão
as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o
máximo de 600 reais. O programa não deve se preocupar com a quantidade
de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas
notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três
notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro
notas de 1.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
valor_saque = int(
    input("Digete o valor pra saque, minimo 10 e o maximo 599: "))
a_1 = "uma"
a_2 = "duas"
a_3 = "três"
a_4 = "quarto"
a_5 = "cinco"
a_6 = "seis"
a_7 = "sete"
a_8 = "oito"
a_9 = "nove"
a_10 = "dez"
saida_final = ""

# ================================================================================
#                           Logica do programa
# ================================================================================
if valor_saque >= 10 and valor_saque < 600:
    # Este comando faz que 10 vire 010 e converte pra str
    valor = "{:0>3}".format(valor_saque)

    """ Converti o valor de int pra str e depois atribuir cada numero pra uma variavel.
        Assim o numero 120 vira a = 1 centena, b = 2"""
    a, b, c = int(valor[0]), int(valor[1]), int(valor[2])

    if a == 1:
        saida_final = "{} nota de 100,".format(a_1)
    elif a == 2:
        saida_final = "{} notas de 100,".format(a_2)
    elif a == 3:
        saida_final = "{} notas de 100,".format(a_3)
    elif a == 4:
        saida_final = "{} notas de 100,".format(a_4)
    elif a == 5:
        saida_final = "{} notas de 100,".format(a_5)

    if b >= 5:
        saida_final += " {} nota de 50,".format(a_1)
        if 5 + 1 == b:
            saida_final += " {} nota de 10,".format(a_1)
        elif 5 + 2 == b:
            saida_final += " {} notas de 10,".format(a_2)
        elif 5 + 3 == b:
            saida_final += " {} notas de 10,".format(a_3)
        elif 5 + 4 == b:
            saida_final += " {} notas de 10,".format(a_4)
    elif b == 1:
        saida_final += " {} nota de 10,".format(a_1)
    elif b == 2:
        saida_final += " {} notas de 10,".format(a_2)
    elif b == 3:
        saida_final += " {} notas de 10,".format(a_3)
    elif b == 4:
        saida_final += " {} notas de 10,".format(a_4)

    if c >= 5:
        saida_final += " {} nota de 5,".format(a_1)
        if 5 + 1 == c:
            saida_final += " {} nota de 1.".format(a_1)
        elif 5 + 2 == c:
            saida_final += " {} notas de 1.".format(a_2)
        elif 5 + 3 == c:
            saida_final += " {} notas de 1.".format(a_3)
        elif 5 + 4 == c:
            saida_final += " {} notas de 1.".format(a_4)
    elif c == 1:
        saida_final += " {} nota de 1.".format(a_1)
    elif c == 2:
        saida_final += " {} notas de 1.".format(a_2)
    elif c == 3:
        saida_final += " {} notas de 1.".format(a_3)
    elif c == 4:
        saida_final += " {} notas de 1.".format(a_4)

    print(saida_final)

else:
    print("Valor Invalido")
