# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
7 - Faça um Programa que calcule a área de um quadrado,
em seguida mostre o dobro desta área para o usuário.
"""

lado_quadrado = int(input("Digite um dos lados do quadrado: "))
area_quadrado = lado_quadrado * 2
dobro = area_quadrado * 2
print("Você Digitou {} então seu Quadrado tem {} e o dobro desta area é {}"
      .format(lado_quadrado, area_quadrado, dobro))
