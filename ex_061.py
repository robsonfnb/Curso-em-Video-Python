print('Progressão Aritmética')
pt = int(input('Informe o primeiro termo: '))
rz = int(input('Informe a razão da PA: '))
termo = 10
c = 1
print(pt, end=' ')
while c < termo:
    print('->', end=' ')
    pt += rz
    c += 1
    print(pt, end=' ')
print('-> FIM')
