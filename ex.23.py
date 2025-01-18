# Solicitando ao Usuário  que insira o número inicial
numero_inicial = int(input("Digite um número inicial: "))

# Solicitando ao usuário que insira um número final
numero_final = int(input("Digite um número final: "))

# Exibindo todos os números entre o número inicial e o número final (inclusive)
print(f"Os números entre {numero_inicial} e {numero_final} são: ")
for i in range(numero_inicial,numero_final + 1):
    print(i)