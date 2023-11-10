print('Pagamento de produto e forma de pagamento')
prod = str(input('Informe o produto: '))
valor = float(input('Informe o valor do produto: R$'))
print('Escolha a forma de pagamento')
print('Digite [1] para pagamento em dinheiro ou cheque com 10% de desc.')
print('Digite [2] para pagamento a vista no cartão com 5% de desc.')
print('Digite [3] para pagamento em até 2x no cartão com preço normal.')
print('Digite [4] para pagamento em até 3x ou mais no cartão com 20% de juros.')
pag = int(input('Digite a opção para pagamento: '))
if pag == 1:
    totvalor = valor - (valor * 10) / 100
    print('O valor total do produto {} será de R${:.2f}. '.format(prod.title(), totvalor))
elif pag == 2:
    totvalor = valor - (valor * 5) / 100
    print('O valor total do produto {} será de R${:.2f}. '.format(prod.title(), totvalor))
elif pag == 3:
    totvalor = valor / 2
    print('O valor total do produto {} será de R${:.2f} e será divido em 2 parcelas de R${:.2f}. '.format(prod.title(), valor, totvalor))
elif pag == 4:
    parcela = int(input('O valor será dividido em quantas parcelas?: '))
    totvalor = (valor + (valor * 20) / 100 ) / parcela
    print('O valor total do produto {} será de R${:.2f} e será divido em {} parcelas de R${:.2f}. '.format(prod.title(), valor, parcela, totvalor))
else:
    print('Opção Inválida de pagamento')

