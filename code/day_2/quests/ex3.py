'''3 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
A. "Telefonou para a vítima?"
B. "Esteve no local do crime?"
C. "Mora perto da vítima?"
D. "Devia para a vítima?"
E. "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada
como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostas = []

for pergunta in perguntas:
    resposta = input(f"{pergunta} (sim ou não): ").lower()
    while resposta != "sim" and resposta != "não":
        print("Resposta inválida. Responda apenas com 'sim' ou 'não'.")
        resposta = input(f"{pergunta} (sim ou não): ").lower()
    respostas.append(resposta)

positivas = respostas.count("sim")

if positivas == 2:
    print("Classificação: Suspeita")
elif 3 <= positivas <= 4:
    print("Classificação: Cúmplice")
elif positivas == 5:
    print("Classificação: Assassino")
else:
    print("Classificação: Inocente")