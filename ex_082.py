principal = list()
impar = list()
par = list()
while True:
    principal.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N}: ')).strip()
    while r not in 'SsNn':
        print('Resposta incorreta!')
        r = str(input('Quer continuar? [S/N}: ')).strip()
    if r in 'Nn':
        break
for pos, num in enumerate(principal):
    if num % 2 == 0:
        par.append(num)
    elif num % 2 == 1:
        impar.append(num)
print(f'Os números digitados foram {principal}')
print(f'Os números pares foram {par}')
print(f'Os números ímpares foram {impar}')
