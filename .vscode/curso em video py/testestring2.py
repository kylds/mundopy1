# que leia o número de 0 a 9999 que mostre na tela cada um dos dígitos separados 
# unidade, dezena, centena, milhar 

 
numero = int(input("Digite o número:"))
#n = str(numero)
n = numero // 1 % 10 #divido um número e pego o resto de uma divisão por 10 
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
# tem que criar outra variável 
# porém tem que ser um número de quatro digítos para funcionar 
print("Analisando o número {}".format(numero))
print("Unidade: {}".format(n))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))
#print("Unidade: {}".format(n[3]))
#print("Dezena: {}".format(n[2]))
#print("Centena: {}".format(n[1]))
#print("Milhar: {}".format(n[0]))

        



        
