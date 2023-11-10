def dobro(n=0, formato=False):
    v = n * 2
    return v if formato is False else moeda(v)


def metade(n=0, formato=False):
    v = n / 2
    return v if formato is False else moeda(v)


def diminuir(n=0, taxa=0, formato=False):
    v = n - (n * taxa / 100)
    return v if formato is False else moeda(v)


def aumentar(n=0, taxa=0, formato=False):
    v = n + (n * taxa / 100)
    return v if formato is False else moeda(v)


def moeda(n=0):
    mf = str(f'R${n:.2f}').replace('.', ',')
    return mf


def resumo(n=0, aum=0, red=0):
    print('-' * 75)
    print('Resumo de Preço'.center(75))
    print('-' * 75)
    print(f'Preço analisado: {moeda(n)}')
    print(f'O dobro de {moeda(n)} é {dobro(n,formato=True)}')
    print(f'A metade de {moeda(n)} é {metade(n,formato=True)}')
    print(f'{moeda(n)} com {aum}% de aumento é igual a {aumentar(n, aum,formato=True )}')
    print(f'{moeda(n)} com {red}% de redução é igual a {diminuir(n,red,formato=True)}')
    print('-' * 75)
