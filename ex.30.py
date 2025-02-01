numero=int(input("Escolhe um número: "))

soma=0

for x in range(1, numero+1):
    soma+=x
    print(x, end=" ")

print()
print(f"A soma de todos os números até {numero} é igual a {soma}.")