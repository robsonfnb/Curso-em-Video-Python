import random
import time
print('---Jogo da adivinhação---')
n = random.randint(1, 5)
print('Acabei de pensar em um número entre 1 e 5, tente adivinha-lo')
resp = int(input('Qual é o seu palpite? '))
print('PROCESSANDO...')
time.sleep(2)
if resp == n:
    print('O número em que eu pensei foi {}. Você acertou, Parabéns!'.format(n))
else:
    print('O número em que eu pensei foi {}. Você errou, mais sorte na próxima!'.format(n))
print('---FIM---')


