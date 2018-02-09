# Telegram: @ZumbiPy __   _ ___
#  /_  / __ ____ _  / /  (_) _ \__ __
#   / /_/ // /  ' \/ _ \/ / ___/ // /
#  /___/\_,_/_/_/_/_.__/_/_/   \_, /
# E-mail: zumbipy@gmail.com   /___//dev - 09/02/2018
"""
45 - Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões,
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o
gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa).
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema.
Após todos os alunos terem respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da
prova antes dos alunos usarem o programa.
"""


def perguntar(lista_perguntas):
    lista_resportas_aluno = []
    for i, pergunta in enumerate(lista_perguntas):
        print(f"{i + 1} - {pergunta}")
        resposta_aluno = input("Digite sua respota: ").lower()
        lista_resportas_aluno.append(resposta_aluno)
        print()
    return lista_resportas_aluno


def corecao(lista_resportas, lista_resportas_aluno):
    nota = 0
    for rperguntas, raluno in zip(lista_resportas, lista_resportas_aluno):
        nota += 1 if rperguntas == raluno else 0
    return nota

# Maior e Menor Acerto;


def maior_menor_acerto(lista_alunos):
    maior, menor = 0, 10
    for aluno in lista_alunos:
        nota = aluno[2]
        maior = nota if nota >= maior else maior
        menor = nota if nota <= menor else menor
    return maior, menor


# A Média das Notas da Turma.
def media_notas(lista_alunos):
    media_notas = sum([nota[2] for nota in lista_alunos]) / len(lista_alunos)
    return media_notas


def gabarito(lista_resportas):
    saida = ""
    for numero, resposta in enumerate(lista_resportas):
        saida += f"{numero + 1:02} - {resposta.upper()}\n"
    return saida


if __name__ == "__main__":
    lista_perguntas = ["""Qual o número mínimo de jogadores numa partida de futebol?

a) 8
b) 10
c) 9
d) 5
e) 7""",
                       """Normalmente, quantos litros de sangue uma pessoa tem? Em média, quantos são retirados numa doação de sangue?

a) Tem entre 2 a 4 litros. São retirados 450 mililitros
b) Tem entre 4 a 6 litros. São retirados 450 mililitros
c) Tem 10 litros. São retirados 2 litros
d) Tem 7 litros. São retirados 1,5 litros
e) Tem 0,5 litros. São retirados 0,5 litros""",
                       """De onde é a invenção do chuveiro elétrico?

a) França
b) Inglaterra
c) Brasil
d) Austrália
e) Itália""",
                       """Quais o menor e o maior país do mundo?

a) Vaticano e Rússia
b) Nauru e China
c) Mônaco e Canadá
d) Malta e Estados Unidos
e) São Marino e Índia
                    """,
                       """Qual o nome do presidente do Brasil que ficou conhecido como Jango?

a) Jânio Quadros
b) Jacinto Anjos
c) Getúlio Vargas
d) João Figueiredo
e) João Goulart""",
                       """Qual o grupo em que todas as palavras foram escritas corretamente?

a) Asterístico, beneficiente, meteorologia, entertido
b) Asterisco, beneficente, meteorologia, entretido
c) Asterisco, beneficente, metereologia, entretido
d) Asterístico, beneficiente, metereologia, entretido
e) Asterisco, beneficiente, metereologia, entretido""",
                       """Qual o livro mais vendido no mundo a seguir à Bíblia?

a) O Senhor dos Anéis
b) Dom Quixote
c) O Pequeno Príncipe
d) Ela, a Feiticeira
e) Um Conto de Duas Cidades""",
                       """Quantas casas decimais tem o número pi?

a) Duas
b) Centenas
c) Trilhares
d) Vinte
e) Milhares""",
                       """Atualmente, quantos elementos químicos a tabela periódica possui?

a) 113
b) 109
c) 108
d) 118
e) 92""",
                       """Quais os países que têm a maior e a menor expectativa de vida do mundo?

a) Japão e Serra Leoa
b) Austrália e Afeganistão
c) Itália e Chade
d) Brasil e Congo
e) Estados Unidos e Angola"""]

    lista_resportas = ["e", "b", "c", "c", "a", "e", "b", "b", "c", "d"]
    lista_alunos = []
    while True:
        nome_aluno = input("Qual seu nome: ")
        respostas = perguntar(lista_perguntas)
        nota = corecao(lista_resportas, respostas)
        lista_alunos.append([nome_aluno, respostas, nota])

        if input("Digite 0 para sair ou Entre para Continuar: ") == "0":
            break

    maior, menor = maior_menor_acerto(lista_alunos)
    total_alunos = len(lista_alunos)
    media = media_notas(lista_alunos)
    saida = gabarito(lista_resportas)
    print()
    print(f"""Total de Alunos que utilizaram o sistema: {total_alunos}
Maior e Menor Acerto: {maior}/{menor}
A Média das Notas da Turma: {media}
Gabarito da Prova:

{saida}
""")
