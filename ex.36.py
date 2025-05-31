from random import randint # importamos uma biblioteca do Python com funções que nos devolvem valores aleatórios (random). Além disso, fomos buscar o randint, que apenas devolve números inteiros de forma aleatória.

while True:
    pc = randint(0,2)  # aqui, usamos o randint para obter 1 valor de entre 3 possíveis, que corresponde a cada jogada que o pc fizer. 0 = pedra; 1 = papel; 2 = tesoura
    jogada = int(input("Pedra, papel, ou tesoura? Escolhe um número entre 0 e 2: "))  # aqui, dependendo do número que escolhermos, vamos jogar contra o pc. A lógica de 0 = pedra; 1 = papel; 2 = tesoura mantém-se.

    if jogada == 0:
        print("Jogaste PEDRA.")
        if pc == 0:
            print("Empate! O PC também jogou PEDRA.")
        elif pc == 1:
            print("Derrota! O PC jogou PAPEL.")
        elif pc == 2:
            print("Vitória! O PC jogou TESOURA.")
            break
    elif jogada == 1:
        print("Jogaste PAPEL.")
        if pc == 0:
            print("Vitória! O PC jogou PEDRA.")
            break
        elif pc == 1:
            print("Empate! O PC também jogou PAPEL.")
        elif pc == 2:
            print("Derrota! O PC jogou TESOURA.")
    elif jogada == 2:
        print("Jogaste TESOURA.")
        if pc == 0:
            print("Derrota! O PC jogou PEDRA.")
        elif pc == 1:
            print("Vitória! O PC jogou PAPEL.")
            break
        elif pc == 2:
            print("Empate! O PC também jogou TESOURA.")
    else:
        print("Jogada inválida.")


