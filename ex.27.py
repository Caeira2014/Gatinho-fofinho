numero_inicial=int(input("Escolha o número inicial: "))
numero_final=int(input("Escolha o número final: "))

par_ímpar=int(input("Quer números pares [1] ou ímpares [2]?: "))

soma=0 #definimos a variável soma para armazenar o somatório dos números

if par_ímpar==1:
    print("Os números pares são: ")

if par_ímpar==2:
    print("Os números ímpares são: ")

# verificação de números pares ou ímpares:

for x in range(numero_inicial,numero_final+1): # faz a contagem de todos os números desde o número inicial ao final
    if par_ímpar==1:
        if x%2==0: # se o resto da divisão for zero, é par
            print(x, end=" ")
            soma+=x # vai somando os números uns aos outros
    elif par_ímpar==2:
        if x%2==1:
            print(x, end=" ")
            soma+=x # vai somando os números uns aos outros
    else:
        print("opção inválida!")
        break

if par_ímpar==1:
    print()
    print(f"A soma de todos os números pares é {soma}.")

elif par_ímpar==2:
    print()
    print(f"A soma de todos os números ímpares é {soma}.")
