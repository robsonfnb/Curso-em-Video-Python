from datetime import date
print('-Alistamento Militar-')
ano = date.today().year
nasc = int(input('Informe o ano do seu nascimento: '))
idade = ano - nasc
print('Você que nasceu em {} tem {} anos em {}'.format(nasc, idade, ano))
if idade < 18:
    saldo = 18 - idade
    print('Você ainda é muito jovem para se alistar')
    print('Ainda faltam {} anos para o seu alistamento'.format(saldo))
    alistamento = ano + saldo
    print('Seu alistamento será em {}'.format(alistamento))
elif idade == 18:
    print('Você já está na idade de fazer o seu alistamento militar, apresente a uma unidade do exercito brasileiro')
else:
    saldo = idade - 18
    print('Você já passou da idade de fazer o alistamento militar, procure uma unidade do exercito mais proximo para regularizar sua situação.')
    print('Você deveria ter se alistado há {} anos atrás'.format(saldo))
    alistamento = ano - saldo
    print('Seu alistamento deveria ter sido feito em {}'.format(alistamento))


