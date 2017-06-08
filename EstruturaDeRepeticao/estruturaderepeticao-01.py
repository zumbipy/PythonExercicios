# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaDeRepeticao
"""
1 - Faça um programa que peça uma nota, entre zero e dez.
    Mostre uma mensagem caso o valor seja inválido e continue pedindo
até que o usuário informe um valor válido.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
# Entrada de Dados.
nota = int(input("Digite uma nota entre 0 e 10: "))

# ================================================================================
#                           Lógica do programa
# ================================================================================
# Loop com While

while True:
    if nota >= 0 and nota <= 11:
        print("Valor Válido!")
        break
    else:
        print("Valor inválido")
        nota = int(input("Digite uma nota entre 0 e 10: "))
