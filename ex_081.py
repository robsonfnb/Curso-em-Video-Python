numeros = list()
cinco = 0
while True:
    n = (int(input('Digite um número: ')))
    numeros.append(n)
    if n == 5:
        cinco += 1
    r = (str(input('Quer continuar? [S/N]: '))).strip()
    while r not in 'SsNn':
        print('Resposta incorreta, tente novamente')
        r = (str(input('Quer continuar? [S/N]: '))).strip()
    if r in 'Nn':
        break
numeros.sort(reverse=True)
print(f'Foram digitados {len(numeros)} números ao todo')
print(f'Os números em ordem decrescente são {numeros}')
if 5 in numeros:
    print(f'O valor 5 foi digitado {cinco} vezes na lista')
else:
    print(f'O valor 5 não foi digitado na lista')



