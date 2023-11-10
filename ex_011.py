print('Vamos calcular quanto litros de tinta serão necessarios para pintar uma parede')
print('Cada litro de tinta é capaz de pintar 2m²')
alt = float(input('Qual é a altura da parede em metros?'))
lar = float(input('Qual é a largura da parede em metros?'))            
area = alt * lar
t = area / 2
print('Para pintar essa parede de {:.3}m²  serão necessarios {}L de tinta'.format(area, t))

