# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaLista
"""
08 - Faça um Programa que peça a idade e a altura de 5 pessoas,
armazene cada informaçãono seu respectivo vetor. Imprima a idade
e a altura na ordem inversa a ordem lida.
"""
v_idade = []
v_altura = []

for i in range(1, 6):
    idade = v_idade.insert(0, input("Digite a idade de {}/5: ".format(i)))
    altura = v_altura.insert(
        0, input("Digite a altura em Cm de {}/5: ".format(i)))
    print()

print()
for idade, altura in zip(v_idade, v_altura):
    print("idade : {}, Altura: {}".format(idade, altura))
