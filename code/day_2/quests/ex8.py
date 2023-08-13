'''8 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
B. A mensagem "Reprovado", se a média for menor do que sete;
C. A mensagem "Aprovado com Distinção", se a média for igual a dez.'''
def resultado_notas (n1,n2):
    media = (n1 + n2)/2
    if media >= 7 and media < 10:
       return "Aprovado!"
    elif media == 10:
        return "Aprovado com Distinção!"
    else:
        return "Reprovado"
    
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

print(resultado_notas(nota1,nota2))