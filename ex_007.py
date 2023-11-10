print('Vamos calcular a média entre as notas de um aluno')
al = str(input('Informe o nome do aluno: '))
n1 = float(input('Informe a 1ª nota do aluno: '))
n2 = float(input('Informe a 2ª nota do aluno: '))
m = (n1 + n2) / 2
print('A média do aluno {} é igual á {:.1f}'. format(al, m))
