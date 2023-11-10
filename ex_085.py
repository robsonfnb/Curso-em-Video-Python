numeros = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Informe o {c}º valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('-=' * 25)
numeros[0].sort()
numeros[1].sort()
print(f'Os numeros pares são: {numeros[0]}')
print(f'Os numeros impares são: {numeros[1]}')
