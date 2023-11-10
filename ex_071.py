from time import sleep
print('-= Banco do povo =-')
nt50 = nt10 = nt5 = nt1 =0
valor = int(input('Qual é o valor do saque? R$ '))
print('Contando cédulas...')
print('-='*25)
sleep(1)
if valor >= 50:
    nt50 = valor // 50
    sobra50 = valor % 50
    print(f'{nt50} notas de R$ 50.00')
else:
    nt50 = 0
    sobra50 = valor % 50
if sobra50 != 0:
    nt10 = sobra50 //10
    sobra10 = sobra50 % 10
    if sobra50 >= 10:
        print(f'{nt10} notas de R$ 10.00')
else:
    nt10 = 0
    sobra10 = sobra50 % 10
if sobra10 != 0:
    nt5 = sobra10 // 5
    sobra5 = sobra10 % 5
    if sobra10 >= 5:
        print(f'{nt5} notas de R$ 5.00')
else:
    nt5 = 0
    sobra5 = sobra10 % 5
if sobra5 != 0:
    nt1 = sobra5
    print(f'{nt1} notas de R$ 1.00')
else:
    nt1 = 0
print(f'Saque no valor de R$ {valor:.2f} efetuado com sucesso')
print('-= Volte Sempre =-')