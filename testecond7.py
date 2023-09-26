# ler o comprimento de três retas e dizer se ele pode ou não formar um triângulo 

a = float(input("Digite um valor:"))
b = float(input("Digite um valor:"))
c = float(input("Digite um valor:"))
if a + b > c:
    b + c > a
    a + c > b 
    print("Com esses valores um triângulo pode ser formado!")
else:
    print("Com esses valores um triângulo não pode ser formado!")
