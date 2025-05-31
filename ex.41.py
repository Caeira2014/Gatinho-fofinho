import math

def escolher_funcao():
    global escolha
    print("0 - sair          1 - Soma          2 - Subtrair")
    print("3- Dividir        4 - Multiplicar   5 - Raiz Quadrada")
    print("6 - Potência      7 - Volume do Prisma       8 - Volume do Cilindro")
    print("9 - Volume Cone    10 - Volume Esfera")
    escolha=int(input("Que operação vais escolher?: "))
def soma():
    r = x+y
    print(f"O resultado da soma é {r}")

def sub():
    r=x-y
    print(f"O resultado da subtração é {f}")

def div():
    r=x/y
    print(f"O resultado da divisão é {r}")

def mult():
    r=x*y
    print(f"O resultado da multiplicação é {r}")
def raiz():
    r=math.sqrt(x)
    print(f"A raiz quadrada de {x} é {r}")

def potencia():
    r = x**y
    print(f"A potência de {x} elevado a {y} é {r}")

def v_prisma():
    r=x*y*z
    print(f"O volume do prima é {r}m3")

def v_cilindro():
    r = math.pi*(x**2)*y
    print(f"O volume do cilindro é {r}")
def v_cone():
    r=(math.pi*(x**2)*y)/3
    print(f"O volume do cone é {r}")

def v_esfera():
    r = (4*math.pi*(x**3))/3
    print(f"O volume da esfera é {r}m3")
while True:
    escolher_funcao()
    if escolha==0:
        break
    elif escolha in [1,4]:
        x = int(input("Escolhe o primeiro número: "))
        y=int(input("Escolhe o segundo número: "))
        if escolha==1:
            soma()
        elif escolha==2:
            sub()
        elif escolha==3:
            div()
        elif escolha==4:
            mult()
        elif escolha==5:
            x=int(input("Escolhe um número para raiz quadrada: "))
            raiz()

    elif escolha==6:
        x=int(input("Escreve um número: "))
        y=int(input("A qual valor o vais elevar?: "))
        potencia()

    elif escolha==7:
        x = int(input("Escreve o valor da largura: "))
        y=int(input("Escreve o valor do Comprimento: "))
        z=int(input("Escreve o valor da Altura: "))
        v_prisma()

    elif escolha in [8,9]:
        x=int(input("Escreve o valor do Raio: "))
        y=int(input("Escreve o valor da Altura: "))
    if escolha==8:
        v_cilindro()
    elif escolha== 9:
        v_cone()
    elif escolha==10:
        x=int(input("Escreve o valor do Raio: "))
        v_esfera()