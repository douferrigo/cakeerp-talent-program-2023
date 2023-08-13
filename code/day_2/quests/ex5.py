'''- Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em
porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.'''

def soma_imposto (taxa_imposto,custo):
    valor = custo + (custo * taxa_imposto / 100)
    return valor

custo_produto = float(input("Qual o custo do produto?"))
imposto = float(input("Digite a taxa do imposto: "))

valor = soma_imposto(custo_produto,imposto)
print("O preço do produto com impostos é :", valor)