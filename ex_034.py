print('Aumento de salário')
print('Para salarios acima de R$ 1250,00 o aumento será de 10%')
print('Para salários inferiores a este valor o aumento será de 15%')
nome = str(input('Qual o nome do funcionário? '))
sal = float(input('Qual é o salario atual do funcionário? R$'))
if sal <= 1250:
    novo = sal + (sal * 15 / 100)
else:
    novo = sal + (sal * 10 / 100)
print('O novo salário do funcionario {} será de R${}'.format(nome, novo))




