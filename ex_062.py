print('Progressão Aritmética Avançada')
pt = int(input('Informe o primeiro termo: '))
rz = int(input('Informe a razão da PA: '))
termo = 10
totc = 0
while termo != 0:
    c = 1
    print(pt, end=' ')
    while c < termo:
        print('->', end=' ')
        pt += rz
        c += 1
        print(pt, end=' ')
    totc += c
    print('-> Pausa')
    termo = int(input('Quantos termos mais você gostaria de ver? '))
    pt += rz
print('A progressão foi finalizada com {} termos mostrados'.format(totc))



