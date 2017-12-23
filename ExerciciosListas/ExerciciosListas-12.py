# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaLista
"""
12 - Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine
quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses
alunos.
"""
l_altura = [1.40, 1.70, 1.55, 1.70, 1.80, 1.79, 1.66, 1.70]
l_idade = [14, 7, 18, 15, 17, 13, 13, 15]
media = 0
soma = 0
a_i_media = 0


for media in l_altura:
    soma += media

media = soma / len(l_altura)

for i in range(len(l_idade)):
    if l_idade[i] > 13 and l_altura[i] < media:
        a_i_media += 1

print(a_i_media)
