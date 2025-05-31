from math import pi #vamos à bilioteca da matemática buscar o valor de pi

raio=float(input("Quanto mede o raio do círculo?: "))

area= pi * (raio**2) #como importamos o pi da biblioteca math, podemos usá-lo como um número no cálculo da área do círculo

print(f"A área do círculo com raio {raio} é de {area}.")