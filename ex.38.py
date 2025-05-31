from random import randint
tentativas=0
pc = randint(0, 5)

while True:
    eu = int(input("Escolhe um número de 0 a 5: "))

    if pc == eu:
        print(f"Parabéns! Você acertou.Foram precisas {tentativas} tentativas para adivinhar")
        break
    else:
        print("Você errou! Tente novamente.")
        tentativas+=1