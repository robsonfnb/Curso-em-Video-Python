lista = list()
while True:
    n = (int(input('Informe um valor: ')))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, não será adicionado')
    resp = str(input('Quer continuar? [S/N]: ')).strip()
    if resp in 'Nn':
        break
    while resp not in 'SsNn':
        print('Esta não é uma opção válida. Informe [S/N]: ')
        resp = str(input('Quer continuar? [S/N]: ')).strip()
print('=-' * 15)
print('Você digitou os seguintes valores', end=' ')
print(sorted(lista))
