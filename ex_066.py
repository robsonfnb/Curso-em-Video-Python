soma = 0
cont = 0
while True:
    n = int(input('Informe um número, digite 999 para sair:  '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'O total de números informados foi {cont} e a soma dos valores resulta em {soma}.')
