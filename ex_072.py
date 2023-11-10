cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
        n = int(input('informe um número de 0 a 20: '))
        if n <0 or n > 20:
                n = int(input('informe um número de 0 a 20: '))
        else:
                break
print(f'Você digitou o número {cont[n]}')








