maior = homem = menos20 = p = 0
while True:
    s = ' '
    while s not in 'MF':
        s = str(input('Informe o sexo. [M/F]: ')).strip().upper()[0]
    if s == 'M':
        homem += 1
    i = int(input('Informe a idade: '))
    if i >= 18:
        maior += 1
    if s == 'F' and i < 20:
        menos20 += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    print('-='*20)
    p += 1
    if r == 'N':
        break
print(f'{p} pessoas foram cadastradas ')
print(f'{maior} pessoas tem mais de 18 anos, {homem} são homens, {menos20} mulheres tem menos de 20 anos')

