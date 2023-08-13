#2 - Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.#
pessoas = []
for i in range(5):
    pessoa = {}
    pessoa['idade'] = int(input("Digite a idade da pessoa: "))
    pessoa['altura'] = float(input("Digite a altura da pessoa: "))
    pessoas.append(pessoa)
for pessoa in reversed (pessoas):
    print(f"Idade: {pessoa['idade']} anos | Altura: {pessoa['altura']:.2f} metros")
