def soma():
    resultado=numero1+numero2
    print(f"A soma entre {numero1} e {numero2} dá {resultado}.")

def subtracao():
    resultado=numero1-numero2
    print(f"A subtração de {numero2} a {numero1} dá {resultado}.")
def multiplicacao():
    resultado=numero1*numero2
    print(f"A multiplicação de {numero1} por {numero2} dá {resultado}.")

def divisão():
    resultado=numero1/numero2
    print(f"A divisão de {numero1} por {numero2} dá {resultado}.")
while True:
    numero1=int(input("Escolhe um número: "))
    numero2=int(input("Escolhe outro número: "))
    operacao=int(input("""Qual é a operação que pretendes fazer com os dois números? Escolhe uma das opções:
[0] - SAIR
[1] - SOMA
[2] - SUBTRAÇÃO
[3] - MULTIPLICAÇÃO
[4] - DIVISÃO"""))
    if operacao==0:
        print("A encerrar...")
        break
    elif operacao==1:
        soma()
    elif operacao==2:
        subtracao()
    elif operacao==3:
        multiplicacao()
    elif operacao==4:
        divisão()
    else:
        print("Operação inválida, tenta outra vez.")
