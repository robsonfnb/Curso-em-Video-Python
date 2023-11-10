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
