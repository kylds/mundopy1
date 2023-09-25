# ler três números e ve qual é o maior e o menor
lista = [] 
for i in range(3):
    num = int(input("Digite um número:"))
    lista.append(num)
print(min(lista))
print(max(lista))
# min para pegar o menor número 
# max para pegar o maior número 
# sum para realizar a soma de todos os elementos da lista 