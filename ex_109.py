from pack_ex_109 import moeda

v = float(input('Informe um valor: R$ '))
print(f'O dobro de {moeda.moeda(v)} é R$ {moeda.dobro(v,True)}')
print(f'A metade de {moeda.moeda(v)} é R$ {moeda.metade(v, True)}')
print(f'{moeda.moeda(v)} com aumento de 15% é igual R$ {moeda.aumentar(v,15, True)}')
print(f'{moeda.moeda(v)} com redução de 15% é igual R$ {moeda.diminuir(v, 15, True)}')