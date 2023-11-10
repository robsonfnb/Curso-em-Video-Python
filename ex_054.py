from datetime import date
maior = 0
menor = 0
atual = date.today().year
for c in range(1, 8):
    nasc = int(input('Informe o nome de nascimento da {}ª pessoa :'.format(c)))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('O total de pessoas que atingiram a maioridade é {}'.format(maior))
print('O total de pessoas que ainda não atingiram a maioridade é {}'.format(menor))
