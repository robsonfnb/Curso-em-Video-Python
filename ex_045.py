import random
print('Vamos jogar jokenpô')
pc = random.choice(['pedra', 'papel', 'tesoura']).title()
jogador = str(input('Escolha entre pedra, papel e tesoura: ')).title()
print('Você escolheu {}'.format(jogador))
print('Computador escolheu {}'.format(pc))
if (jogador == 'Pedra') and (pc == 'Tesoura') or (jogador == 'Papel') and (pc == 'Pedra') or (jogador == 'Tesoura') and (pc == 'Papel'):
    print('Parabéns! Você Venceu')
elif (jogador == 'Pedra') and (pc == 'Pedra') or (jogador == 'Papel') and (pc == 'Papel') or (jogador == 'Tesoura') and (pc == 'Tesoura'):
    print('Empatou')
elif (jogador == 'Pedra') and (pc == 'Papel') or (jogador == 'Papel') and (pc == 'Tesoura') or (jogador == 'Tesoura') and (pc == 'Pedra'):
    print('O Computador ganhou =/ ')










