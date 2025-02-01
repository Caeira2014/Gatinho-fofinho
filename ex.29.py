maior = menor = 0

for x in range(1, 6):
    peso = int(input(f"Insere o {x}º peso: "))
    if x == 1:
        maior = menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print()
print(f"O número maior é {maior}.")
print(f"O número menor é {menor}.")