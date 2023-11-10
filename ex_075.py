num = (int(input('Informe um número: ')),
int(input('Informe outro número: ')),
int(input('Informe mais um número: ')),
int(input('Informe o último número: ')))
print(f'Você digitou os valores {num}')
print(f'O número 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)+1}ª posição')
else:
    print(f'O valor 3 não foi informado em nenhuma posição')
print(f'Os números pares digitados foram os números ', end='')
for n in num:
    if n % 2 == 0:
        print(n, '.', end='')










