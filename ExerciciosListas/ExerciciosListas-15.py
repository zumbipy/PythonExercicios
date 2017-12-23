# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaLista
"""
15 - Faça um programa que leia um número indeterminado de valores,
correspondentes a notas, encerrando a entrada de dados quando for
informado um valor igual a -1 (que não deve ser
armazenado). Após esta entrada de dados, faça:
a. Mostre a quantidade de valores que foram lidos;
b. Exiba todos os valores na ordem em que foram informados, um ao lado do
outro;
c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo
do outro;
d. Calcule e mostre a soma dos valores;
e. Calcule e mostre a média dos valores;
f. Calcule e mostre a quantidade de valores acima da média calculada;
g. Calcule e mostre a quantidade de valores abixo de sete;
h. Encerre o programa com uma mensagem;
"""
num = None
vetor_notas = [0]
media = 0
soma = 0
total_index = None
total_index = 0
v_baixo_sete = 0
v_maior_media = 0

while True:
    num = int(input("Digite uma nota 0 ateé 10 ou -1 ára sair: "))
    # Condição de parada.
    # Condition of stop.
    if num == -1:
        break
    # Verifica se o valor é menor que dez (10).
    # Check if value is smaller of ten (10).
    if num > 10 or num < -1:
        print("Valor inválido!!!")
        continue

    vetor_notas.append(num)
    soma += num
total_index = len(vetor_notas)
media = soma / total_index
print()


print("A. Mostre a quantidade de valores que foram lidos.")

print("Total de Números digitados foi: ", total_index)
print()

print("B. Exiba todos os valores na ordem em que foram informados,um ao lado do outro.")
for num in vetor_notas:
    print(num, end=" ")

print()
print()

print ("C. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro.")
for num in range((total_index - 1), -1, -1):
    print(vetor_notas[num])
print()
print()

print("D. Calcule e mostre a soma dos valores.")
print("Total da soma das notas: ", soma)
print()

print("E. Calcule e mostre a média dos valores.")
print("A média dos valores foi: ", media)
print()

print("F. Calcule e mostre a quantidade de valores acima da média calculada.")
for num in vetor_notas:
    if num > media:
        v_maior_media += 1
print("Quantidade de calores acima da média foi : ", v_maior_media)
print()

print("G. Calcule e mostre a quantidade de valores abixo de sete")
for num in vetor_notas:
    if num < 7:
        v_baixo_sete += 1
print("Quantidade de valores abaico de sete foi: ", v_baixo_sete)
print()

print("H. Encerre o programa com uma mensagem;")
print("Finalindo o programa ^^,")

print
