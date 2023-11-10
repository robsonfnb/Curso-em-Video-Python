pessoas = list()
dados = list()
print('Vamos cadastrar nome e peso e filtrar pessoas entre mais leves e mais pesadas')
print('Condiderando as mais leves com peso abaixo de 60kg')
print('Condiderando as mais pesadas com peso acima de 90kg')
pesado = leve = ' '
while True:
    nome = str(input('Informe o nome:'))
    dados.append(nome)
    peso = float(input('informe o peso (Kg): '))
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()
    r = str(input('Quer continuar? [S/N]: '))
    while r not in 'SsNn':
        r = str(input('Resposta Inváida! Quer continuar? [S/N]: '))
    if r in 'Nn':
        break
for p in pessoas:
    if p[1] >= 90:
        pesado += p[0]
    if p[1] <= 60:
        leve += p[0]
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'As pessoas mais pesadas da lista são: {pesado}')
print(f'As pessoas mais leves da lista são: {leve}')



