print('Mercadão Zika da Balada')
valor = caro = soma = item = menor = 0
barato = ' '
while True:
    prod = str(input('Informe o produto: '))
    valor = float(input('informe o valor R$:'))
    item += 1
    soma += valor
    if valor >= 1000:
        caro += 1
    if item == 1 or valor < menor:
        menor = valor
        barato = prod
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
print(f'Foram selecionados {item} produtos somando um valor de R$ {soma:.2f}')
print(f'{caro} produtos custam mais de R$ 1000,00')
print(f'O produto mais barato é {barato} que custa R$ {menor:.2f}')
print('{:-^100}'.format(' Fim do Programa '))




