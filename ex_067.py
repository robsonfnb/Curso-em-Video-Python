c = 0
while True:
    n = int(input('Quer ver a tabuada de que número? '))
    if n < 0:
        break
    for c in range(1, 11):
        r = c * n
        print(f'{n} x {c:2} = {r:2}')
        c += 1
    print('_-' * 20)
print('Programa encerrado, Volte Sempre')
