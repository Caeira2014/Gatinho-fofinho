#------------CICLO FOR-----------------

#enquanto que os ciclos WHILE correm infinitamente, o ciclo FOR existe para quando queremos controlar a QUANTIDADE DE ITERAÇÕES (repetições) que faz.
#nos ciclos FOR existe um dado que monitoriza as vezes que eles se repetem chamado VARIÁVEL DE ITERAÇÃO
#depois, basta-nos definir qual é o dado que vai limitar a repetição do ciclo, que pode ser uma variável de qualquer tipo ou uma string

#o ciclo vai-se repetir de acordo com o ÍNDICE dos dados que inserirmos, ou seja, por exemplo, a quantidade de carateres num dado de texto (string), a quantidade de elementos numa lista (ÍNDICE DE CADA ELEMENTO DA LISTA), entre outros
#o ÍNDICE, em python, é a ORDEM em que um elemento está, que começa a contar do ZERO (0)

#----------EXEMPLO + LÓGICA DA ESTRUTURA-----------
# VARIÁVEL DE ITERAÇÃO, ou seja o elemento que vai PERCORRER O SEGUNDO ELEMENTO DO CICLO
#   |    SEGUNDO ELEMENTO DO CICLO, ou seja, o PARÂMETRO que LIMITA A QUANTIDADE DE ITERAÇÕES DO CICLO
#   |       |    a palavra TESTE tem 5 LETRAS. o primeiro carater da palavra tem ÍNDICE 0
#   v       v
for x in "TESTE": #aqui, dá-se a avaliação da condição, ou seja, a variável de iteração x vai percorrer a palavra TESTE
    print(x)      #aqui, por cada ITERAÇÃO, ou seja, CADA VEZ QUE A VARIÁVEL DE ITERAÇÃO PERCORRE UMA LETRA, O CICLO CONTINUA ATÉ AS LETRAS ACABAREM

# contudo, mesmo que o ciclo FOR tenha um número de ITERAÇÕES definido, podemos interrompê-lo a qualquer altura
# para tal, basta indicarmos o comando BREAK!
# de modo a inserir esta instrução, devemos indicar as condições sob as quais o nosso ciclo deve parar!
#por exemplo:
for v in "SHARKCODERS": #aqui, a VARIÁVEL DE ITERAÇÃO VAI PERCORRER A PALAVRA
    print(v)
    if v=="O": #inserimos a condição de quebra
        break  #mandamos o ciclo parar, ou seja, interrompemos