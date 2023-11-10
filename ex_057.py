sex = str(input('Informe o seu sexo, M para Masculino ou F para Feminino: ')).strip().upper()[0]
while sex != 'M' and sex != 'F':
    print('Comando inválido, tente novamente')
    sex = str(input('M para masculino ou F para feminino: ')).strip().upper()[0]
if sex == 'M':
    sex = 'Masculino'
if sex == 'F':
    sex = 'Feminino'
print('Entendi você é do sexo {}'.format(sex))

