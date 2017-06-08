# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaDeRepeticao
"""
23 - Faça um programa que mostre todos os primos entre 1 e N.
sendo N um número inteiro fornecido pelo usuário. O programa
deverá mostrar também o número de divisões que ele executou
para encontrar os números primos. Serão avaliados o funcionamento,
o estilo e o número de testes (divisões) executados.
"""
# ================================================================================
#                                      Variavel.
# ================================================================================
numero = int(input("Digite um numero: ")) + 1
contado_zero = 0
contado_divisao = 0
total_numero_primos = ""

# ================================================================================
#                                      Logica.
# ================================================================================
# Percorre um lista do 2 ao numero digita.
for lista in range(2, numero):
    contado_zero = 0
    # se o numero for par != 2, ele pula tudo e volta por primeiro for.
    if lista % 2 == 0 and lista != 2:
        continue
    # Verificar se o Numero e Primo.
    for numeros in range(1, lista + 1):
        contado_divisao += 1
        if lista % numeros == 0:
            contado_zero += 1
        if contado_zero > 2:
            break
    else:
        total_numero_primos += "{}, ".format(lista)

print("Lista de Numero Pirmo de 1 ate {}".format(numero))
# Coloca ponto final no ultimo numero
total_numero_primos = total_numero_primos[:len(total_numero_primos) - 2] + "."
print(total_numero_primos)
print("Total de Divisoes:")
print(contado_divisao)
