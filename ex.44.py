from random import randint

vidalutador1=3
vidalutador2=3
fim=False

while not fim:
   forcalutador1=randint(0,3)
   forcalutador2 = randint(0, 3)
   print("Força lutador1: ",forcalutador1, " Força lutador2: ",forcalutador2)
   if forcalutador1> forcalutador2:
       vidalutador2=vidalutador2-1
       print("Nesta ganhou o lutador 1")
   elif forcalutador1 < forcalutador2:
       vidalutador1=vidalutador1-1
       print("Nesta ganhou o lutador 2")
   else:
       print("Nesta empataram os lutadores com força: ",forcalutador1)
   print("Vidas Lutador 1:",vidalutador1)
   print("Vidas Lutador 2:", vidalutador2)
   if vidalutador2==0 or vidalutador1==0:
       fim = True



