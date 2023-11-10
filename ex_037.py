print('Conversor Numérico')
n = int(input('Informe um número inteiro: '))
escolha = int(input('Para Binário digite [1] , Para Octal digite [2] e para Hexadecimal digite [3]: '))
if escolha == 1:
    print('{} convertido para Binario é igual {}'.format(n, bin(n)[2:]))
elif escolha == 2:
    print('{} convertido em Octagonal é igual a {}'.format(n, oct(n)[2:]))
elif escolha == 3:
    print('{} convertido em Hexadeciaml é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Esta não é uma opção válida')
    



