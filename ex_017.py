import math
co = float(input('Informe a medida do cateto oposto: '))
ca = float(input('informe a medida do cateto adjascente: '))
hip = math.hypot(co, ca)
print('A hipotenusa tem o valor de {:.2f}'.format(hip))