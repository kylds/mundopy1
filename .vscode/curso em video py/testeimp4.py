import random 
lista = []
lista2 = []
aluno = str(input("Digite um nome:"))
lista.append(aluno)
aluno2 = str(input("Digite um nome:"))
lista.append(aluno2)
aluno3 = str(input("Digite um nome:"))
lista.append(aluno3)
aluno4 = str(input("Digite um nome:"))
lista.append(aluno4)


for i in range(1,5):
    escolha = random.choice(lista)
    lista.index(escolha)
    lista2.append(escolha)
    lista.remove(escolha)
print("A ordem é {}".format(lista2))