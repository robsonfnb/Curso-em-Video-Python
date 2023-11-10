n = str(input('informe um número entre 0 ate 9999: '))
if len(n)>4:
    print('O número informado excede a quantidade permitida pelo sistema')
elif len(n)==4:
    print('Unidade = {}'.format(n[3]))
    print('Dezena = {}'.format(n[2]))
    print('Centena = {}'.format(n[1]))
    print('Milhar = {}'.format(n[0]))
elif len(n)==3:
    print('Unidade = {}'.format(n[2]))
    print('Dezena = {}'.format(n[1]))
    print('Centena = {}'.format(n[0]))
    print('Milhar = 0')
elif len(n)==2:
    print('Unidade = {}'.format(n[1]))
    print('Dezena = {}'.format(n[0]))
    print('Centena = 0')
    print('Milhar = 0')
elif len(n)==1:
    print('Unidade = {}'.format(n[0]))
    print('Dezena = 0')
    print('Centena = 0')
    print('Milhar = 0')





