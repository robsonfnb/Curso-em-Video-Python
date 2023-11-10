from time import sleep
c = ('\033[31m',
        '\033[32m',
        '\033[34m',
        '\033[36m',
        '\033[35m',
        '\033[33m',
        '\033[30m')

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 2)
    print(c[3], end=' ')
    help(com)
    print(c[3], end=' ')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end=' ')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end=' ')
    sleep(1)


#Programa Principal
comando = ' '
while True:
    titulo('Sistema de ajuda Pyhelp', 2)
    comando = str(input('Função ou biblioteca -> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Ate logo!', 4)
