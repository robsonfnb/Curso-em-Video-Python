print('Vamos calcular quanto ficou a despesa do aluguel de um carro:')
print('Diária= R$60,00 e R$ 0,15 por Km Rodado')
dias = int(input('Por quantos dias o veículo foi alugado?'))
km = float(input('Quantos km foram percorridos com o veículo?'))
valor = (dias * 60) + (km * 0.15)
print('O veículo foi alugado por {} dias e percorreu {:.1f} km, então o total a ser pago é o valor de R${:.2f}'.format(dias, km, valor))
