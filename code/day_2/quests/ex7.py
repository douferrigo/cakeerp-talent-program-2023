'''7 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''

while(True):
    sexo = str(input("Digite o seu sexo: F - Feminino ou M - Masculino")).upper()
    if (sexo == 'F'):
        print("F - Feminino")
        break
    elif (sexo == 'M'):
        print("M - Masculino")
        break
    else:
        print("Sexo inválido.")