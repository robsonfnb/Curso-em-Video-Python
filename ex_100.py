from random import randint
from time import sleep
lista = list()
def sorteia():
    for c in range(1, 6):
        n = randint(1, 10)
        c += 1
        lista.append(n)
        sleep(0.5)
        print(f'{n}', end=' ')
    print('FIM')


def somapar():
    pares = 0
    for n in lista:
        if n % 2 == 0:
            pares += n
    print(f'A soma dos números pares da lista {lista} resulta em: {pares}')


print('-= Sorteando 5 números da lista =-')
print('-' * 34)
sorteia()
somapar()
