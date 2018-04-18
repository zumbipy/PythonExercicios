# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
3 - Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
nome = None
idade = None
salario = None
sexo = None
estado_civil = None

# ================================================================================
#                           Logica do programa
# ================================================================================
# Entada do dado Nome e Verifica se e tem mais de 3 letras.
nome = input("Digite seu nome: ")
while len(nome) <= 3:
    print("!!!ERRO!!! Nome tem que te mais de 3 letras.")
    nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))
while idade > 0 and idade <= 150:
    print("!!!ERRO!!! Idade não permitida.")
    idade = int(input("Digite sua idade: "))

salario = float(input("Digite seu salario: "))
while salario <= 0:
    print("!!!ERRO!!! Salario tem que se maior que 0")
    salario = float(input("Digite seu salario: "))

sexo = input("Digite (F) Feminino ou (M) Masculino: ")
while True:
    if "feminino".startswith(sexo.lower()):
        sexo = "Feminino"
        break
    elif "masculino".startswith(sexo.lower()):
        sexo = "Masculino"
        break
    else:
        print("!!!ERRO!!! Valor Inválido")
        sexo = input("Digite (F) Feminino ou (M) Masculino: ")

estado_civil = input("Qual seu estado civil (S), (C), (V), (D): ")
while True:
    if estado_civil.lower() == "s":
        estado_civil = "(S)"
        break
    elif estado_civil.lower() == "c":
        estado_civil = "(C)"
        break
    elif estado_civil.lower() == "v":
        estado_civil = "(V)"
        break
    elif estado_civil.lower() == "d":
        estado_civil = "(D)"
        break
    else:
        print("!!!ERRO!!! Valor Inválido")
        estado_civil = input("Qual seu estado civil (S), (C), (V), (D): ")
    