print('Vamos descobrir o dobro, o triplo e a raiz quadrada de um número informado por você')
n = int(input('Informe um número: '))
d = n * 2
t = n * 3
r = n**(1/2)
print('O dobro do número {} é o número {}, seu triplo é {} e a sua raiz quadrada é {:.2f}'.format(n, d, t, r))
# A raiz quadrada também pode ser calculada usando o comando pow(n, (1/2)) #
