''' Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos. '''
def soma(num1, num2, num3):
    return num1 + num2 + num3
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

resultado = soma(n1,n2,n3)
print(f"O resultado é: {resultado}")