nome = str(input('Digite seu nome completo: ')).strip()
formatado = (nome.title())
print('Seu nome tem Miranda? {}'.format('Miranda' in formatado))
#Também pode ser feito da forma abaixo:
#print('Seu nome tem Miranda? {}.format('miranda in nome.lower()))

