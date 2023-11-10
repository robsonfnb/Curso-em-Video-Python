lista = ('programaçao', 'profissional', 'trabalho', 'futuro', 'familia', 'vida', 'oportunidade', 'mudança')
for palavra in lista:
    print(f'\nNa palavra {palavra.upper()} temos ', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')




