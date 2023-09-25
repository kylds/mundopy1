# salario de funcionario e calcular o aumento 
# superior a 1250 10% de aumento e inferiores 15%
salario = float(input('Digite o salário:'))
if salario > 1250:
    #como calcular aumento em py
    percentual = 10/100
    aumento = percentual * salario
    novo_s = salario + aumento
    print("O aumento salarial será de R$ {}".format(novo_s))
else:
    percentual = 15/100
    aumento = percentual * salario
    novo_s = salario + aumento
    print("O aumento salarial será de R$ {}".format(novo_s))