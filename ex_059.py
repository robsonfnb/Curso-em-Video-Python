print('Menu de opções:')
n1 = float(input('Informe um número: '))
n2 = float(input('Informe mais um número: '))
resp = 0
while resp != 5:
    print('[1] para somar')
    print('[2] para multiplicar')
    print('[3] para saber o maior')
    print('[4] para novos números')
    print('[5] para sair')
    resp = int(input('Qual é a sua opção: '))
    if resp == 1:
        s = n1 + n2
        print('A soma entre {} e {} é igual a {}'.format(n1, n2, s))
        print('-------------------------------------------------')
    elif resp == 2:
        m = n1 * n2
        print('A multiplicação entre {} e {} é igual a {}'.format(n1, n2, m))
        print('-------------------------------------------------')
    elif resp == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número entre {} e {} é o número {}'.format(n1, n2, maior))
        print('-------------------------------------------------')
    if resp == 4:
        n1 = float(input('Informe um número: '))
        n2 = float(input('Informe mais um número: '))
    else:
        print('Opção inválida')
print('Terminou')

