from random import randint
from time import sleep


def maior():
    vezes = randint(1, 10)
    print('Analisando os valores sorteados.')
    print('-=' * 20)
    maior = 0
    for c in range(1, vezes):
        num = randint(0, 100)
        sleep(0.5)
        print(f'{num}', end=' ')
        if c == 1:
            maior = num
            c += 1
        else:
            if num > maior:
                maior = num
                c += 1
    print('FIM')
    print(f'Ao todo foram informados {c} valores.')
    print(f'O maior número sorteado foi o número:{maior}.')
    print('-=' * 20)


maior()


