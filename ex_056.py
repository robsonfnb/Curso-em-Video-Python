idade = 0
somaidade = 0
menor20 = 0
velho = ' '
for p in range(1,5):
    n = str(input('Informe o nome da {}ª pessoa: '.format(p))).upper().strip()
    i = int(input('Informe a idade: '))
    s = str(input('Informe o sexo [M] Masculino ou [F] Feminino: ').upper()).strip()
    somaidade += i
    if s == 'M':
        if i > idade:
            idade += i
            velho = n
    if s == 'F':
        if i < 20:
            menor20 += 1
media = somaidade / 4
print(' A média de idade do grupo é de {}'.format(media))
print('O homem mais velho é {} com {} anos'.format(velho, idade))
print('O total de mulheres com menos de 20 anos é/são {} pessoas'.format(menor20))




