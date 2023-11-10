print('Média de um aluno')
n1 = float(input('Informe a 1ª nota do aluno: '))
n2 = float(input('Informe a 2ª nota do aluno: '))
m = (n1 + n2) / 2
print('A média do aluno foi {:.1f}'.format(m))
if m < 5:
    print('Aluno reprovado')
elif (m >= 5) and (m < 7):
    print('Aluno em recuperação')
elif m >= 7:
    print('Aluno aprovado')

