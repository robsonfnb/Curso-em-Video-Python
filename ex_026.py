frase = str(input('Digite uma frase qualquer e vamos ver quantas letras A aparecem nela: ')).strip()
formatado = frase.upper()
print('A letra A aparece {} vezes nesta frase e aparece pela primeira vez na {}ª posição e por último na {}ª posição'.format(formatado.count('A'), formatado.find('A')+1, formatado.rfind('A')+1))


