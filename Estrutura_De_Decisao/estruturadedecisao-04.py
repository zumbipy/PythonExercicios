# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaDeDecisao
# Para execurta o programa on line entra no link a baixo:
# https://repl.it/I0iN/2
"""
4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
# Entrada de Dados.
letra_digitada = input("Digite uma letra: ").lower()

# Verefica se letra_digita esta dentro de vogais
if letra_digitada == "a":
    print("esta letra e uma vogal")
elif letra_digitada == "e":
    print("esta letra e uma vogal")
elif letra_digitada == "i":
    print("esta letra e uma vogal")
elif letra_digitada == "o":
    print("esta letra e uma vogal")
elif letra_digitada == "u":
    print("esta letra e uma vogal")
else:
    print("esta letra e uma consoante")
