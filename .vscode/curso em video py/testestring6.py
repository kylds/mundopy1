#ler o nome completo mostrando o primeiro e ultimo nome separado 
# ana maria de souza, primeiro = Ana, ultimo = Souza 

nome = str(input("Digite o seu nome completo:")).strip()
d = nome.split()
print("Seu primeiro nome é {}".format(d[0]))
print("Seu último nome é {}".format(d[len(d)-1]))