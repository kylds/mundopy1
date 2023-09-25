km = int(input("Quantos km foram percorridos:"))
trans = km * 0.15 
dias = int(input("Por quantos dias o carro foi alugado:"))
quant = dias * 60
total = trans + quant 
print("A quantia que deve ser paga é R$ {}".format(total))
