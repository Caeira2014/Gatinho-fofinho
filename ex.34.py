def encontraLetra():
    soma=0
    frase=input("Escreve uma frase: ")
    letra=input("Que letra desejas procurar?: ")

    for x in frase:
        if x == letra:
            soma+=1
    print(f"Esta frase tem {soma} letras {letra}.")

encontraLetra()
