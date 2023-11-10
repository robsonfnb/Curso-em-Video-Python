n = str(input(' Digite seu nome completo: '))
print('Analisando seu nome')
print('Seu nome em maiúsculo: {}'.format(n.upper()))
print('Seu nome em minúsculo: {}'.format(n.lower()))
n.split()
print('Seu nome tem {} letras'.format(len(n) - n.count(' ')))
print('Seu primeiro nome tem {} letras'.format(n.find(' ')))
separa = n.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))











