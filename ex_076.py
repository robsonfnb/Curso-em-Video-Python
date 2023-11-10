listagem = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00, 'Estojo', 25.00, 'Mochila', 120.00)
print('-' * 60)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-' * 60)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<50}', end=' ')
    else:
        print(f'R${listagem[pos]:>5.2f}')
print('-' * 60)
