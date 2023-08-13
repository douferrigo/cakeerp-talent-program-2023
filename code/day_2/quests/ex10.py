'''- As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que
calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário
atual:
A. salários até R$ 280,00 (incluindo) : aumento de 20%
B. salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
C. salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
D. salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
E. o salário antes do reajuste;
F. o percentual de aumento aplicado;
G. o valor do aumento;
H. o novo salário, após o aumento.'''

def aumento_salario (salario):
    if salario <= 280:
        salario_novo = salario + (salario * 20/100)
        return(f"Salário antes do reajuste: {salario:.2f}",
            "Percentual de aumento: 20%",
            f"Valor do aumento: {salario_novo - salario:.2f}",
            f"Salário novo: {salario_novo:.2f}") 
    elif salario > 280 and salario < 700:
        salario_novo = salario + (salario * 15/100)
        return(f"Salário antes do reajuste: {salario:.2f}",
            "Percentual de aumento: 15%",
            f"Valor do aumento: {salario_novo - salario:.2f}",
            f"Salário novo: {salario_novo:.2f}")
    elif salario > 700 and salario < 1500:
        salario_novo = salario + (salario * 10/100)
        return(f"Salário antes do reajuste: {salario:.2f}",
            "Percentual de aumento: 10%",
            f"Valor do aumento: {salario_novo - salario:.2f}",
            f"Salário novo: {salario_novo:.2f}")
    else:
        salario_novo = salario + (salario * 5/100)
        return(f"Salário antes do reajuste: {salario:.2f}",
            "Percentual de aumento: 5%",
            f"Valor do aumento: {salario_novo - salario:.2f}",
            f"Salário novo: {salario_novo:.2f}")
    

salario_atual = float(input("Digite o seu salário atual: "))
print(aumento_salario(salario_atual))