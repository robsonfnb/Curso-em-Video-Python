from pack_ex_108 import moeda

v = float(input('Informe um valor: R$ '))
print(f'O dobro de {moeda.moeda(v)} é {moeda.moeda(moeda.dobro(v))}')
print(f'A metade de {moeda.moeda(v)} é {moeda.moeda(moeda.metade(v))}')
print(f'{moeda.moeda(v)} com aumento de 15% é igual {moeda.moeda(moeda.aumentar(v, 15))}')
print(f'{moeda.moeda(v)} com redução de 15% é igual {moeda.moeda(moeda.diminuir(v, 15))}')
