print('Vamos dar um desconto de 5% em um determinado produto')
p = float(input('Informe o valor do produto que vai receber o desconto: R$'))
d = float(p*5/100)
nv = float(p - d)
print('o novo valor do produto será R${:.2f}'.format(nv))
        
