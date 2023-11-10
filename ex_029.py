print('Radar Eletrônico')
print('O Limite de velocidade é 80km/h e a multa é de R$7,00 por km ultrapassado')
v = int(input('Informe a velocidade em que o veículo passou pelo radar: '))
if v > 80:
    m = (v - 80) * 7
    print('O veículo passou a {}km/h pelo radar e a multa será de R${:.2f}'.format(v, m))
else:
    print('O veículo passou dentro do limite de velocidade e não será multado')

