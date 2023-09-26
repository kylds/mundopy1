# ler o nome de uma cidade e dizer se começa ou não com a palavra SANTO 

cidade = str(input("Digite o nome da cidade:")).strip()
print(cidade[:5].upper() == 'SANTO')
# a palavra Santo tem 4 letras contando com o espaço
# o upper é para digitar de qualquer forma SANTO 