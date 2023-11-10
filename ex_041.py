from datetime import date
print('Classificação dos atletas em categorias pela sua idade')
print('Até 9 anos = Mirim')
print('Até 14 anos = Infantil')
print('Até 19 anos = Junior')
print('Até 25 anos = Senior')
print('Aciam de 25 anos = Master')
ano = date.today().year
nasc = int(input('Qual é o seu ano de nascimento?: '))
categoria = ano - nasc
if categoria <= 9:
    print('Atleta da categoria mirim')
elif categoria <= 14:
    print('Atleta da categoria Infantil')
elif categoria <= 19:
    print('Atleta da categoria Junior')
elif categoria <= 25:
    print('Atleata da categoria Senior')
elif categoria > 25:
    print('Atleta da categoria Master')

