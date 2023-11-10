soma = 0
qt = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        qt = qt + 1
        soma = soma + num
print('Soma destes {} números é igual a {}'.format(qt, soma))
print('FIM')



