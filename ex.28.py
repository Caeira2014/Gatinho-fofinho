europa=["portugal", "espanha", "frança", "bélgica", "inglaterra"] #para criarmos uma lista, basta criar uma variável, abrir parêntesis retos [] e adicionar os nossos elementos separados por uma vírgula# (,)

for x in range(3):
    escolha=input("Tenta adivinhar um país da Europa que esteja na nossa lista: ")
    if escolha in europa:  #usammos IN na nossa condicional para verificar se a nossa escolha está DENTRO (IN) da variável europa, que é uma LISTA. para verificar o conteúdo de uma lista, usamos IN
        print("Parabéns!")
        break
    else:
        print("Não está na lista.")