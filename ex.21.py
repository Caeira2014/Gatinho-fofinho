x = int(input("Escreve um número: "))
soma=0

while True:
    soma+=x
    x=int(input("Escreve mais um número"))
    if soma>=150:
        break

print("Memória cheia! A soma de todos os números chegou a: ", soma)