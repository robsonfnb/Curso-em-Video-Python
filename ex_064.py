n = 0
tot = 0
c = 0
print('informe números para serem somados, digite 999 para sair. ')
while n != 999:
    n = int(input('Informe um número: '))
    if n != 999:
        tot += n
        c += 1
print('Foram digitados {} números e a soma deles é {}'.format(c, tot))



