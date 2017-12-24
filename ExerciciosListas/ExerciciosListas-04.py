# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
04 - Faça um Programa que leia um vetor de 10 caracteres,
e diga quantas consoantes foram lidas. Imprima as consoantes.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
vetor_letras = ["d", "a", "f", "e", "t", "y", "o", "k", "d", "c"]
vetor_consoantes = []
vetor_vogais = ["a", "e", "i", "o", "u"]

# ================================================================================
#                           Logica do programa
# ================================================================================
print("lista de Letras: ")
for i in vetor_letras:
    # Verifica se a letra não é vogal e add a lista.
    if i not in vetor_vogais:
        vetor_consoantes.append(i)
    print(i, end="")

print()
print()

print("Lista da Consoantes:")
for letra in vetor_consoantes:
    print(letra, end="")
print()
