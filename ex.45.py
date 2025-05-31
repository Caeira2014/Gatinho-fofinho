from random import randint

while True:
    pc = randint(1,3)
    jogada = int(input("Pedra ,Papel ou Tesoura? Diz um número de 1 a 3: "))

    if jogada == 1:
        print("Jogaste PEDRA.")
        if pc == 1:
            print("Empate! O PC também jogou PEDRA.")
        elif pc == 1:
            print("Derrota! O PC jogou PAPEL.")
        elif pc == 1:
            print("Vitória! O PC jogou TESOURA.")
            break
    elif jogada == 2:
        print("Jogaste PAPEL.")
        if pc == 1:
            print("Vitória! O PC jogou PEDRA.")
            break
        elif pc == 2:
            print("Empate! O PC também jogou PApel")
        elif pc == 2:
            print("Derrota! O PC jogou TESOURA.")
    elif jogada == 3:
        print("Jogaste TESOURA.")
        if pc == 1:
            print("Derrota! O PC jogou PEDRA.")
        elif pc == 2:
            print("Vitória! O PC jogou PAPEL.")
            break
        elif pc == 3:
            print("Empate! O PC também jogou TESOURA.")
    else:
        print("Jogada inválida.")





