#vê a distância de uma viagem em km
#calcular o preço da passagem cobrando 0.50 por km para viagens até 200 km
#e 0.45 se ultrpassar 200 km

dist = float(input("Digite a distância em km:"))
if dist <= 200:
    pas =  dist * 0.50
    print("Distância de {} km".format(dist))
    print("O valor do preço da passagem é R$ {}".format(pas))
else:
    # cada km vai custa 45 centavos 
    pas = dist * 0.45
    print("Distância de {} km".format(dist))
    print("O valor do preço da passagem é R$ {}".format(pas))

