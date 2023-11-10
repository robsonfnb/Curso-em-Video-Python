print('Números Primos')
np = int(input('Informe um número: '))
tot = 0
for c in range(1, np + 1):
    if np % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(np, tot))
if tot == 2:
    print('E por isso ele é Primo')
else:
    print('E por isso ele NÃO é Primo')



