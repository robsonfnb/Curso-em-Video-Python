from pack_ex_107 import moeda

v = float(input('Informe um valor: R$ '))
print(f'O dobro de {v} é R$ {moeda.dobro(v)}')
print(f'A metade de {v} é R$ {moeda.metade(v)}')
print(f'{v} com aumento de 15% é igual R$ {moeda.aumentar(v,15)}')
print(f'{v} com redução de 15% é igual R$ {moeda.diminuir(v, 15)}')
