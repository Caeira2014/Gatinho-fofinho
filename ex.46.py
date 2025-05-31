numero_inicial=int(input("Escolha o número inicial: (ou prime x para parar)"))
numero_final=int(input("Escolha o número final: "))

par_impar=int(input("Quer números pares [1] ou ímpares [2]?: "))

soma=0

if par_impar==1:
    print("Os números pares são: ")

if par_impar==2:
    print("Os números ímpares são: ")

for x in range(numero_inicial,numero_final+1):
    if par_impar==1:
        if x%2==0:
            print(x, end=" ")
            soma+=x
    elif par_impar==2:
        if x%2==1:
            print(x, end=" ")
            soma+=x
    else:
        print("opção inválida!")
        break

if par_impar==1:
    print()
    print(f"A soma de todos os números pares é {soma}.")

elif par_impar==2:
    print()
    print(f"A soma de todos os números ímpares é {soma}")