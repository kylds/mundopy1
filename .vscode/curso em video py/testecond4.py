# ler um ano qualquer e ver se ele é bissexto
from datetime import date 
ano = int(input("Digite o ano! \n Se quiser o ano atual digite 0:"))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("Esse ano é bissexto!")
elif ano == 0:
    ano = date.today().year #para analisar o ano em que estamos atualmente 
    #biblioteca datetime 
else:
    print("Esse ano não é bissexto!")
