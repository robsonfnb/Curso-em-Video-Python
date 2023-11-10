def ficha(jog ='<desconhecido>', gol = 0 ):
    print(f'o jogador {jog} fez {gol} gols no campeonato.')


# Programa principal
n= str(input('Informe o nome do jogador: '))
g = str(input('Informe o número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol = g)
else:
    ficha(n, g)
