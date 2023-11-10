c = 0
num = int(input('A tabuada de qual número você quer saber?: '))
for c in range(1, 11):
    r = c * num
    print('{} x {:2} = {:2}'.format(num, c, r))
    c += 1
print('Fim')
