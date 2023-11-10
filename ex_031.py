print('Vamos calcular o preço da sua passagem')
print('Para viagens até 200km de distancia o preço é R$0,50 por km')
print('Para viagens acima de 200km de distancia o preço é R$0,45 por km')
dis = float(input('Informe a distancia em km do seu destino:'))
if dis <= 200:
    v = dis * 0.5
    print('O valor da sua passagem será de R${:.2f} para {} km de distancia'.format(v, dis))
else:
    v = dis * 0.45
    print('O valor da sua passagem será de R${:.2f} para {} km de distancia'.format(v, dis))
print('---FIM---')



