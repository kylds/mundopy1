#crie um programa que leia o nome completo de alguém e mostre
#o nome com todas as letras maiusculas
#com todas as letra minusculas
#quantas letras possui ao todo (sem contar os espaços)
#quantas letras tem o primeiro nome 


nome = str(input("Digite seu nome completo:")).strip() #pode usar strip já aqui 
print(nome.upper())
print(nome.lower())
print("Esse nome possui {} letras ao todo".format(len(nome)-nome.count(' ')))
# primeira maneira de fazer:
# print("O primeiro nome tem {} letras".format(nome.find(' '))) 
separa = nome.split()
print(separa)
print("Seu primeiro nome é {}".format(separa[0], len(separa[0])))
# segunda maneira de fazer: s
# esse separa vai colocar o nome separado em uma lista
# separa[0] vai pegar apenas o primeiro nome 
# len(separa[0]) vai contar quantas letras tem o primeiro nome 
