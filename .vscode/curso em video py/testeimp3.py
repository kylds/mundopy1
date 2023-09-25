import random 
aluno = str(input("Digite um nome:"))
aluno2 = str(input("Digite um nome:"))
aluno3 = str(input("Digite um nome:"))
aluno4 = str(input("Digite um nome:"))
escolha = random.randint(1,4)
if escolha == 1:
    print("O aluno escolhido foi o {}".format(aluno))
elif escolha ==2:
    print("O aluno escolhido foi o {}".format(aluno2))
elif escolha ==3:
    print("O aluno escolhido foi o {}".format(aluno3))
else:
    print("O aluno escolhido foi o {}".format(aluno4))

