import random
print('---Jogo da adivinhação---')
n = random.randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10, tente adivinha-lo')
resp = int(input('Qual é o seu palpite? '))
chance = 1
while resp != n:
    resp = int(input('Você errou tente outra vez: '))
    chance += 1
else:
    print('Você Acertou! Eu havia pensado no número {}'.format(n))
    print('Você precisou de {} tentativas até acertar'.format(chance))
print('---FIM---')

