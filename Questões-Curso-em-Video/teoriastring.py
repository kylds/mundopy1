frase = "Curso em vídeo"
#fatiamento de string 
print(frase[9]) #vai printar a nona letra de "Curso em vídeo"
print(frase[9:13]) #vai pegar do 9-12 por que ele exclui o 13 
print(frase[9:21:2]) #vai pegar do 9-20 pulando de 2 em 2 
print(frase[:5]) #vai pegar até antes do 5 
print(frase[15:]) #vai pegar do 15 até o final 
print(frase[9::3]) #vai começar do 9 até o final pulando 3 
#ánalise 
len(frase) #comprimento da frase ou o tanto de caracteres que tem na frase
frase.count('o') #vai contar quantas vezes aparece a letra "o"
frase.count('o',0,13) #vai contar quantas letras 'o' tem entre os caracteres 0-13
frase.find('deo') #quantas vezes encontra 'deo'
frase.find("android") #vai procurar se essa string tem, se não tiver retorna o valor -1 por que ele não achou
'Curso' in frase #vai procurar se a palavra curso ta dentro da variável
#transformação
frase.replace('vídeo','android') #vai substituir a palavra vídeo por androids
frase.upper() #o que ja for maiusculo mantém, o que não for ele coloca em maiusculo
frase.lower() #faz o contrário do upper 
frase.capitalize() #vai jogar todos os caraceteres para minusculo menos a primeira letra
frase.title() #transforma a primeira letra de uma palavra em maiusculo
frase.strip() #vai remover os espaços inúteis
frase.rstrip() #r de direita, remove os espaços inúteis da direita e mantém os da esquerda
frase.lstrip() #l de esquerda, faz o contrário do rstrip 
#divisão
frase.split() #aonde tiver espaço ele vai dividir 
'-'.join(frase) #vai colocar um - nos espaços entre as palvaras 