from math import trunc
num = float(input('Informe um número real que vamos te mostrar a parte inteira dele: '))
print('A parte inteira do número {} é igual a {}'.format(num, trunc(num)))

''' 
usando o comando int desta vez ao invés de importar a biblioteca math:

num= float(input('Informe um número real que vamos te mostrar a parte inteira dele: '))
print('A parte inteira do número {} é igual a {}'.format(num, int(num)))
'''

