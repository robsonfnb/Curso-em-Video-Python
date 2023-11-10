dados = dict()
dados['nome'] = str(input('informe o nome do aluno: '))
dados['media'] = float(input('Infome a média do aluno: '))
if dados['media'] >= 7:
    dados['situacao'] = 'Aprovado'
else:
    dados['situacao'] = 'Reprovado'
print(f'Nome é igual a {dados["nome"]}')
print(f'Média é igual a {dados["media"]}')
print(f'Situação é igual a {dados["situacao"]}')

