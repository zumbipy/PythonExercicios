# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaDeRepeticao
"""
09 - Faça um programa que imprima na tela apenas os números
ímpares entre 1 e 50.
"""
# ================================================================================
#                           Logica do Programa.
# ================================================================================
for i in range(1, 50):
    # Quando resto de uma divisao por 2 for 0 ele e par se nao e ímpar.
    if i % 2 != 0:
        print(i)
print("=" * 72)

# ou

for i in range(1, 50, 2):
    print(i)
