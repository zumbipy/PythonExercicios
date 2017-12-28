# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 25/12/2017
"""
36 - Desenvolva um programa que faça a tabuada de um número qualquer inteiro que
será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar
em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo
usuário, conforme exemplo abaixo:
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor que o inicia
"""

monta_tabuada = int(input("monta_tabuada a tabuada de: "))
inicio = int(input("Começa por: "))
terminar = int(input("Terminar em: "))

while True:
    if terminar < inicio:
        print("Terminar não pode se maior que o inicio!!!")
        inicio = int(input("Começa por: "))
        terminar = int(input("Terminar em: "))
    else:
        break

print(f"Vou montar a tabuada de {monta_tabuada} começando em {inicio} e terminando em {terminar}:")
for m in range(inicio, terminar + 1):
    print(f"{monta_tabuada} X {m} = {monta_tabuada*m}")
