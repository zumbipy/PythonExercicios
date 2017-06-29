# # author: ZumbiPy
# # E-mail: zumbipy@gmail.com
# # Exercicio do site http://wiki.python.org.br/EstruturaSequencial
# """
# 26 - Numa eleição existem três candidatos. Faça um programa que peça
# o número total de eleitores. Peça para cada eleitor votar e ao final
# mostrar o número de votos de cada candidato.
# """
# ================================================================================
#                              Variaveis.
# ================================================================================
eleitor = int(input("Digite o numero de eleiores: "))
candidato0 = 0
candidato1 = 0
candidato2 = 0

# ================================================================================
#                           Logica.
# ================================================================================
for i in range(eleitor):
    votos = int(input("""Digite seu voto.
        Canditado 1 - Digite 1.
        Cantidado 2 - Digite 2.
        Cantidado 3 - Digite 3.: """))
    while True:
        if votos <= 0 or votos >= 4:
            print("Voto Invalido!!!")
            votos = int(input("""Digite seu voto.
        Canditado 1 - Digite 1.
        Cantidado 2 - Digite 2.
        Cantidado 3 - Digite 3.: """))
        else:
            break
    # Verifica o voto o soma pra o candidato corrento.
    if votos == 1:
        candidato0 += 1
    elif votos == 2:
        candidato1 += 1
    else:
        candidato2 += 1

print("""
Tabela de votos Computaod
Candiddato 1 teve {} votos.
Candiddato 2 teve {} votos.
Candiddato 3 teve {} votos.""".format(candidato0, candidato1, candidato2))
