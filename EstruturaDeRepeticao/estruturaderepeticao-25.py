# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaDeRepeticao
"""
25 - Faça um programa que peça para n pessoas a sua idade, ao final
o programa devera verificar se a média de idade da turma varia
entre 0 e 26 e 60 e maior que 60; e então, dizer se a turma é
jovem, adulta ou idosa, conforme a média calculada.
"""
# ================================================================================
#                                      Variaveis.
# ================================================================================
pergunta = input("Digite sua Idade ou (s) para sair: ").upper()
total_idade = 0
media = 0

# ================================================================================
#                               Lógica.
# ================================================================================
while True:
    if pergunta == "S":
        break
    else:
        idade = int(pergunta)

    total_idade += idade
    media += 1
    pergunta = input("Digite sua Idade ou (s) para sair: ").upper()

media = total_idade / media

# Comparaçoes que o exercico perdi.
if media <= 26:
    print("A turma é Jovem")
elif media <= 60:
    print("A turma é Adulta")
else:
    print("A turma e Idosa")
