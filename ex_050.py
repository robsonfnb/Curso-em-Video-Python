p = 0
soma = 0
for c in range(1, 7):
    n = int(input('Informe o {}º número: '.format(c)))
    if n % 2 == 0:
        p += 1
        soma += n
print('A soma dos {} números pares é igual á {}'.format(p, soma))

