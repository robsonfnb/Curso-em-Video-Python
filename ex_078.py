lista = [ ]
maior = menor = 0
for c in range(0, 5):
   lista.append(int(input(f'informe um número na posição {c}: ')))
   if c == 0:
       maior = menor = lista[c]
   else:
       if lista[c] > maior:
           maior = lista[c]
       if lista[c] < menor:
           menor = lista[c]
   c += 1
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end=' ')
for num, valor in enumerate(lista):
    if valor == maior:
        print(f'{num}...', end=' ')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end=' ')
for num, valor in enumerate(lista):
    if valor == menor:
        print(f'{num}...', end=' ')





