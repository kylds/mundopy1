import math
ctoposto = float(input("Digite o valor do cateto oposto:"))
ctadja = float(input("Digite o valor do cateto adjacente:"))
hipotenusa = math.pow(ctoposto,2) + math.pow(ctadja,2)
valor = math.sqrt(hipotenusa)
print("O valor da hipotenusa do triângulo é {:.2f}".format(valor))