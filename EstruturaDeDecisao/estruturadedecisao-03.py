# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
# Entrada de Dados.
letra_digitada = input("Digite F - Feminino e M - masculino: ").lower()

# Variáveis
f = "feminino"
m = "masculino"

# logica de comparação
if m.startswith(letra_digitada):
    print(m.capitalize())
elif f.startswith(letra_digitada):
    print(f.capitalize())
else:
    print("Sexo Inválido")
