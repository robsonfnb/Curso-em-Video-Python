print('Será que forma um triangulo? Vamos analisar')
a = float(input('Informe a 1ª medida: '))
b = float(input('Informe a 2ª medida: '))
c = float(input('Informe a 3ª medida: '))
if a <= b + c and b <= a + c and c <= a +b:
    print('Estas medidas formam um triângulo')
else:
    print('Estas medidas não formam um triângulo')
