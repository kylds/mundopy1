# vê a velocidade do carro
# ultrapassar 80 km foi multado se n
# multa 7 reais a cada km excedente, precisa fazer o cálculo
vel = float(input("Digite a velocidade atual:"))
if vel > 80:
    print("Você foi multado! você ultrapassou 80 km/h")
    multa = (vel - 80) * 7
    print("Multa de R$ {:.1f}".format(multa))
else:
    print("Você não foi multado, tenha um bom dia!")