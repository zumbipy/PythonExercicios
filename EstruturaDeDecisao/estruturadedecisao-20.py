# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
20 - Faça um Programa para leitura de três notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e presentar:
a. A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva
média alcançada.
b. A mensagem "Reprovado", se a média for menor do que 7, com a respectiva
média alcançada.
c. A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
# Entrada de Dados.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3

# ================================================================================
#                           Logica do programa
# ================================================================================
if media == 10:
    print("Você foi \"Aprovado cDistinção\" sua nota foi {:.2f}".format(
        media))

elif media >= 7:
    print("Você foi \"Aprovado\" sua nota foi {:.2f}".format(media))

else:
    print("Você foi \"Reprovado\" sua nota foi {:.2f}".format(media))
