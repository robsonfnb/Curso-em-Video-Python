nome = str(input('Digite seu nome completo: ')).strip()
formatado = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {} e o ultimo é {}'.format(formatado[0].title(), formatado[len(formatado)-1].title()))









