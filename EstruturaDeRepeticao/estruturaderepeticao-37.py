# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 27/12/2017
"""
37 - Uma academia deseja fazer um senso entre seus clientes para descobrir o
mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer
um programa que pergunte a cada um dos clientes da academia seu código, sua
altura e seu peso. O final da digitação de dados deve ser dada quando o usuário
digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados
os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais
magro, além da média das alturas e dos pesos dos clientes
"""
codigo_cliente = int(input("Digite seu código: "))
altura_cliente = float(input("Digite sua altura em cm: "))
peso_cliente = float(input("Digite o seu peso: "))
lista_clientes = []

mais_gordo = 0
mais_magro = 100
mais_alto = 0
mais_baixo = 300
media_alturas = 0
media_pesos = 0

# Loop para pega as informações e adicionar a lista_clientes.
while True:
    lista_clientes.append([codigo_cliente, altura_cliente, peso_cliente])
    print("-" * 50)
    codigo_cliente = int(input("Digite seu código: "))
    if codigo_cliente == 0:
        print("-" * 50)
        print("-" * 50)
        break
    altura_cliente = float(input("Digite sua altura em cm: "))
    peso_cliente = float(input("Digite o seu peso: "))

# Aqui fazendos a logica se um e mais gordo e se um e mais magro.
for gordo_magro in lista_clientes:
    peso = gordo_magro[2]
    if peso > mais_gordo:
        mais_gordo = peso
    else:
        pass

    if peso < mais_magro:
        mais_magro = peso
    else:
        pass
    media_pesos += peso

# Aqui fazendos a logica se um e mais alto e se um e mais baixo.
for alto_baixo in lista_clientes:
    altura = alto_baixo[1]

    if altura > mais_alto:
        mais_alto = altura
    else:
        pass

    if altura < mais_baixo:
        mais_baixo = altura
    else:
        pass

    media_alturas += altura

# Calcula a media, usando len() pra sabe quantos clientes foram registrado.
media_alturas /= len(lista_clientes)
media_pesos /= len(lista_clientes)

print(f"Mais pesado teve {mais_gordo}kg e o mais leve teve {mais_magro}kg")
print(f"Mais alto teve {mais_alto}cm e o mais baixo teve {mais_baixo}cm")
print(f"Media de alturas foi {media_alturas}")
print(f"Media de peso foi {media_pesos}")
