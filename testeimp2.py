import math 
angulo = float(input("Digite o valor do ângulo:"))
#para calcular tem que passar o valor do ângulo para radiano
rad = math.radians(angulo)
cos = math.cos(rad)
seno = math.sin(rad)
tan = math.tan(rad)
print("O ângulo {} tem:".format(angulo))
print("Cosseno: {:.2f} \n Seno: {:.2f} \n Tangente: {:.2f}".format(cos,seno,tan))