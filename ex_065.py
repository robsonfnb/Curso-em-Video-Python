resp = 'S'
c = 0
soma = 0
med = 0
menor = 0
maior = 0
while resp == 'S':
    n = int(input('Digite um número: '))
    soma += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
med = soma / c
print('Você digitou {} números e a média deles é {:.2f}'.format(c, med))
print('O maior número informado foi {} e o menor foi {}'.format(maior, menor))



