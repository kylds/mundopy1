# digitar uma frase e mostrar 
# quantas vezes aparece a letra 'a'
# em que posição ela aparece a primeira vez 
#em que posição aparece a última vez 

frase = str(input("Digite uma frase:")).strip()
print("A letra 'a' aparece {} vezes na frase".format(frase.count('a')))
print("Primeira posição de 'a' é {}".format(frase.find('a')))
print("Á último letra 'a' aparece {}".format(frase.rfind('a'))) 
