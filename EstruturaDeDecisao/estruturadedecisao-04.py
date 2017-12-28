# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
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

# ou
print("")
if letra_digitada in ["a", 'e', 'i', 'o', "u"]:
    print(f"A letra [{letra_digitada}] é uma Vogal.")
else:
    print(f"letra [{letra_digitada}] é uma Consoante.")
