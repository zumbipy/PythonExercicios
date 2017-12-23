# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
15 - Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um
triângulo. Indique, caso os lados formem um triângulo,
se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for

maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
# Entrada de Dados
lado_a = int(input("Digite o primeiro lado: "))
lado_b = int(input("Digite o segundo lado: "))
lado_c = int(input("Digite o terceiro lado: "))

# ================================================================================
#                           Logica do programa
# ================================================================================
if lado_a <= 0 or lado_b <= 0 or lado_c <= 0:
    print("não e triagulo")
else:
    if lado_a == lado_b == lado_c:
        print("Triagulo Equilátero")
    elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_b:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
