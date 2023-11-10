l1 = [[], [], []]
l2 = [[], [], []]
l3 = [[], [], []]
n = 0
for c in range(0, 3):
    n = int(input(f'Informe um valor para [0, {c}]: '))
    l1[c].append(n)
for c in range(0, 3):
    n = int(input(f'Informe um valor para [1, {c}]: '))
    l2[c].append(n)
for c in range(0, 3):
    n = int(input(f'Informe um valor para [2, {c}]: '))
    l3[c].append(n)
print(l1[0], l1[1], l1[2])
print(l2[0], l2[1], l2[2])
print(l3[0], l3[1], l3[2])


