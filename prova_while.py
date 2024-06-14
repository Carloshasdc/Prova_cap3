tentativa = 0
import random
numero_secreto = random.randint( 1, 10)
maximo = 3
while tentativa != numero_secreto and maximo > 0 :
      tentativa = int(input("Adivinhe o numero entre 1 e 10: "))
      maximo  -= 1
      if tentativa> 10:
          print(f"{tentativa} fora de escala. Adivinhe o numero entre 10: ")
          maximo += 1
          
      if tentativa > numero_secreto:
          print(f"Muito Alta. Tentativas restantes: {maximo}")
      elif tentativa < numero_secreto and tentativa >= 1:
          print(f"Muito baixa. Tentativas restantes: {maximo}")
      
if tentativa == numero_secreto:
    print("Parabens!, você acertou o  numero secreto")
else:
    print(f"Suas tentativas acabaram. O numero secreto é: {numero_secreto}")