# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___/
"""
19 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a
quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre
outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320,
310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""
# ================================================================================
#                           Variáveis do programa
# ================================================================================
n = int(input("Digite qlq numero: "))

# variaveis vazia.
centena = None
dezena = None
unidade = None
final = None

# ================================================================================
#                           Logica do programa
# ================================================================================
'''
    Aqui uso a divisao pra tira o resto dos numero e depois pego o resto e tiro do
valor atual.
    ex:
    120
    120 / 100 = 1 centena
    120 - (1 * 100) = 20
    20 / 10 = 2 dezenas
    20 - (2 * 10) = 0
    Tem como fazer de outros metodos acredito eu kkkk.
'''
centena = n // 100
n -= centena * 100
dezena = n // 10
n -= dezena * 10
unidade = n

# Comparações.
if centena == 1 and dezena == 0 and unidade == 0:
    final = "{} centena.".format(centena)
elif centena > 1 and dezena == 0 and unidade == 0:
    final = "{} centenas.".format(centena)

elif centena == 1 and dezena == 1 and unidade == 0:
    final = "{} centena e {} dezena.".format(centena, dezena)
elif centena > 1 and dezena == 1 and unidade == 0:
    final = "{} centenas e {} dezena.".format(centena, dezena)
elif centena > 1 and dezena > 1 and unidade == 0:
    final = "{} centenas e {} dezenas.".format(centena, dezena)
elif centena == 1 and dezena > 1 and unidade == 0:
    final = "{} centena e {} dezenas.".format(centena, dezena)

elif centena == 1 and dezena == 0 and unidade == 1:
    final = "{} centena e {} unidade.".format(centena, unidade)
elif centena > 1 and dezena == 0 and unidade == 1:
    final = "{} centenas e {} unidade.".format(centena, unidade)
elif centena > 1 and dezena == 0 and unidade > 1:
    final = "{} centenas e {} unidades.".format(centena, unidade)
elif centena == 1 and dezena == 0 and unidade > 1:
    final = "{} centena e {} unidades.".format(centena, unidade)

elif centena == 1 and dezena == 1 and unidade == 1:
    final = "{} centena, {} dezena e {} unidade.".format(
        centena, dezena, unidade)
elif centena > 1 and dezena == 1 and unidade == 1:
    final = "{} centenas, {} dezena e {} unidade.".format(
        centena, dezena, unidade)
elif centena > 1 and dezena > 1 and unidade == 1:
    final = "{} centenas, {} dezenas e {} unidade".format(
        centena, dezena, unidade)
elif centena > 1 and dezena > 1 and unidade > 1:
    final = "{} centenas, {} dezenas e {} unidades".format(
        centena, dezena, unidade)
elif centena > 1 and dezena == 1 and unidade > 1:
    final = "{} centenas, {} dezena e {} unidades".format(
        centena, dezena, unidade)
elif centena == 1 and dezena == 1 and unidade > 1:
    final = "{} centena, {} dezena e {} unidades".format(
        centena, dezena, unidade)

elif dezena == 1 and unidade == 0:
    final = "{} dezena.".format(dezena)

elif dezena > 1 and unidade == 0:
    final = "{} dezenas.".format(dezena)

elif centena == 0 and dezena == 1 and unidade == 1:
    final = "{} dezena e {} unidade.".format(dezena, unidade)
elif centena == 0 and dezena > 1 and unidade == 1:
    final = "{} dezenas e {} unidade.".format(dezena, unidade)
elif centena == 0 and dezena > 1 and unidade > 1:
    final = "{} dezenas e {} unidades.".format(dezena, unidade)
elif centena == 0 and dezena == 1 and unidade > 1:
    final = "{} dezena e {} unidades.".format(dezena, unidade)

elif unidade == 1:
    final = "{} unidade.".format(unidade)

elif unidade > 1:
    final = "{} unidades".format(unidade)
print(final)
