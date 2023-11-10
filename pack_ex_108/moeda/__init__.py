def dobro(n=0):
    v = n * 2
    return v


def metade(n=0):
    v = n / 2
    return v


def diminuir(n=0, taxa=0):
    v = n - (n * taxa / 100)
    return v


def aumentar(n=0, taxa=0):
    v = n + (n * taxa / 100)
    return v

def moeda(n=0):
    mf = str(f'R${n:.2f}').replace('.', ',')
    return mf



