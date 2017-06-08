# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaDeRepeticao
"""
 7 - Faça um programa que leia 5 números e informe o maior número.
"""
# ================================================================================
#                            Variaveis do Programa
# ================================================================================
numero = None
numero1 = 0
# Esta variavel salva o valor da maior.
f_numero = 0

# ================================================================================
#                           Logica do Programa
# ================================================================================
# Aqui uso uma variavel f_numerocomo acumulador.
for i in range(1, 6):
    numero = int(input("Digite o numero {} de 5: ".format(i)))
    if numero >= numero1:
        numero = numero
    else:
        numero = numero1
    numero1 = numero

print(numero)
