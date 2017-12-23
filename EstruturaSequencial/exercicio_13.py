# author: ZumbiPy
# E-mail: zumbipy@gmail.com
# Exercicio do site http://wiki.python.org.br/EstruturaSequencial
"""
13 - Tendo como dados de entrada a altura e o sexo de uma pessoa,
construa um algoritmo que calcule seu peso ideal, utilizando as
seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7 (h = altura)
Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.
"""

altura = float(input("Digite sua altura em Cm: ")) / 100
sexo = input("Digite M (mulher) ou H (Homem): ").lower()
peso = float(input("Digite sua peso: "))
respota = None
peso_ideal = 0

if "homem".startswith(sexo):
    print("homem")
    peso_ideal = round(72.7 * altura - 58)
    if peso_ideal == peso:
        respota = """Sua altura é {}.
Seu peso é {:.0f}kg e Você esta (dentro) do seu peso
ideal que é {:.0f}kg""".format(altura, peso, peso_ideal)

    elif peso < peso_ideal:
        respota = """Sua altura é {}.
Seu peso é {:.0f}kg e Você esta (abaixo) do seu peso
ideal que é {:.0f}kg""".format(altura, peso, peso_ideal)

    else:
        respota = """Sua altura é {}.
Seu peso é {:.0f}kg e Você esta (acima) do seu peso
ideal que é  {:.0f}kg""".format(altura, peso, peso_ideal)

elif "mulher".startswith(sexo):
    print("mulher")
    peso_ideal = round(62.1 * altura - 44.7)
    if peso_ideal == peso:
        respota = """Sua altura é {}.
Seu peso é {:.0f}kg e Você esta (dentro) do seu peso
ideal que é {:.0f}kg""".format(altura, peso, peso_ideal)

    elif peso < peso_ideal:
        respota = """Sua altura é {}.
        Seu peso é {:.0f}kg e Você esta (abaixo) do seu peso
ideal que é {:.0f}kg""".format(altura, peso, peso_ideal)

    else:
        respota = """Sua altura é {}.
Seu peso é {:.0f}kg e Você esta (acima) do seu peso
ideal que é  {:.0f}kg""".format(altura, peso, peso_ideal)

print(respota)
