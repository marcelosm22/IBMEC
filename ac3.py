#1. Uma empresa resolveu dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo a tabela a seguir, baseado no salário atual. Após o aumento ser realizado, informe na tela: O salário antes do reajuste; O percentual de aumento aplicado; O valor do aumento; O novo salário, após o aumento.

def exercicio_1(salario):
    if salario <= 280:
        porcentagem = 20
    elif salario <= 700:
        porcentagem = 15
    elif salario <= 1500:
        porcentagem = 10
    else:
        porcentagem = 5

    novo_salario = (salario * porcentagem) / 100

    print(salario)
    print(porcentagem, "%")
    print(novo_salario)
    print(salario + novo_salario)

exercicio_1(1400)

#2. Implementa uma função que receba um número e exiba o dia correspondente da semana (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.


def exercicio_2(dia):
    match dia:
        case 1:
            print("Domingo")
        case 2:
            print("Segunda-Feira")
        case 3:
            print("Terça-Feira")
        case 4:
            print("Quarta-Feira")
        case 5:
            print("Quinta-Feira")
        case 6:
            print("Sexta-Feira")
        case 7:
            print("Sábado")
        case _:
            print("Valor inválido")

exercicio_2(3)

#3.Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax^2 + bx + c. O programa deverá receber os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações: Se o usuário informar o valor de a igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado; Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa; Se o delta calculado for igual a zero a equação possui apenas uma raiz real, informe-a ao usuário; Se o delta for positivo, a equação possui duas raízes reais, informe-as ao usuário.


def exercicio_3(a, b, c):
    delta = (b * b) - (4 * a * c)
    bhaskara_positive = (- b + (delta ** (1/2))) / (2 * a)
    bhaskara_negative = (- b - (delta ** (1/2))) / (2 * a)

    if a == 0:
        print("não é de segundo grau")
    elif delta < 0:
        print("não possui raizes reais")
    elif delta == 0:
        print("possui apenas uma raiz:", bhaskara_positive)
    else:
        print("possui duas raizes:", bhaskara_positive, bhaskara_negative)


exercicio_3(2, -1, -2)