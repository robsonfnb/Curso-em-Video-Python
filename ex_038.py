print('Comparando números:')
n1 = int(input('Informe o 1º número: '))
n2 = int(input('Informe o 2º número: '))
if n1 > n2:
    print('O primeiro número informado, no caso o número {} é maior.'.format(n1))
elif n1 < n2:
    print('O segundo número, no caso o número {} é o maior.'.format(n2))
else:
    print('O primeiro e o segundo número são iguais.')
