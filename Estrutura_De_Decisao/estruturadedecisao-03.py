# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaDeDecisao
# Para execurta o programa on line entra no link a baixo:
# https://repl.it/I0ho/0
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
