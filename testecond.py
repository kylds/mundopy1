#escrever um programa para o pc pensar em um número entre 0 e 5 e o usuário tem que adivinhar o npumero e vê se acertou ou não
import random
from time import sleep 
print(20* '-=-')
print("Vou pensar em um número de 0 a 5...")
print(20* '-=-')
numero = int(input("Em que número eu pensei?"))
print("PROCESSANDO")
sleep(3) #para esperar três segundos antes de continuar o programe
num = random.randint(0,5)
if num == numero:
    print("Parabéns, você acertou o número!")
else:
    print("Você não acertou o número!")
