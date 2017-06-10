# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaDeDecisao
# Para execurta o programa on line entra no link a baixo:
# https://repl.it/I0i8/2
"""
5 - Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
# Entrada de Dados.
nota0 = int(input("Digite a Pimeira nota: "))
nota1 = int(input("Digite a Segunda nota: "))
media = (nota0 + nota1) / 2

# Comparações das notas.
if media < 7:
    print("Sua nota é {} então vc foi {}".format(media, "Reprovado"))
elif media == 10:
    print("Sua nota é {} então vc foi {}".format(
        media, "Aprovado com Distrinção"))
else:
    print("Sua nota é {} então vc foi {}".format(media, "Aprovado"))
