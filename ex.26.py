#-VERIFICAÇÃO DE NÚMERO PAR/ÍMPAR COM CICLO FOR

numero=int(input("Escolhe um número: "))

divisoes=0 #esta variável serve para verificarmos se o número é divisível por 1 e por ele próprio, ou seja, 2 vezes. se forem efetuadas mais do que 2 divisões, deixa de ser número primo!
for x in range(1,numero+1): #colocamos sempre +1 para garantir que as iterações vão até ao número escolhido. caso contrário, irão para o número anterior, visto que a contagem começa do zero
    if numero%x==0: #estamos a verificar o resto da divisão entre o número escolhido e todos os números até ele, que são contados pela variável de iteração
        divisoes+=1 #sempre que der resto zero, ou seja, o número for divisível, vamos adicionar 1 contagem às nossas divisões
        print(x, end=" ")
if divisoes > 2:  # se o número tiver mais do que 2 divisões, já não é número primo!
     print(f"O número {numero} não é número primo! Foi divisível {divisoes} vezes!")
 else:
      print(f"O número {numero} é número primo! Foi divisível {divisoes} vezes!")