from random import randint
c = 0
while True:
    pc = randint(1, 100)
    jog = int(input('Escolha um número: '))
    esc = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    if esc == 'P':
        if (pc + jog) % 2 == 0:
            print(f'O computador escolheu {pc} e você escolheu {jog}')
            print(f'O número é {pc + jog} então você venceu')
            c += 1
            print('-='*20)
        else:
            break
    if esc == 'I':
        if (pc + jog) % 2 != 0:
            print(f'O computador escolheu {pc} e você escolheu {jog}')
            print(f'O número é {pc + jog} então você venceu')
            print('-='*20)
            c += 1
        else:
            break
print(f'O computador escolheu {pc} e você escolheu {jog}')
print(f'O número é {pc + jog} então você perdeu')
print(f'Você venceu {c} rodadas')
print('-='*20)




