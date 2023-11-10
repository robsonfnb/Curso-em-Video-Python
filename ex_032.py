from datetime import date
print('Análise de anos bissextos')
ano = int(input('Informe o ano que deseja analisar, digite 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year # Este comando pega a data atual e considera somente o Ano.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))



