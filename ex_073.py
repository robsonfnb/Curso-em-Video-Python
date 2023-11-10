tabela = ('sao paulo', 'corinthians', 'santos', 'palmeiras', 'flamengo', 'fluminense', 'atletico pr', 'atletico mg','chapecoense', 'bahia'
          , 'vitoria', 'gremio', 'sao caetano', 'ponte preta', 'goias', 'vasco', 'botafogo', 'bragantino', 'fortaleza', 'internacional')
print(' -= Campeonato brasileiro =- ')
print('-'*30)
for clube in tabela:
    print(clube)
print(f'Os 5 primeiros colocados são {tabela[0:5]}')
print(f'Os 4 últimos colocados são {tabela[-4:]}')
print(f'Tabela em ordem alfabética', sorted(tabela))
print(f'O time da chapecoense está na {tabela.index("chapecoense") +1 }ª posição na tabela')



