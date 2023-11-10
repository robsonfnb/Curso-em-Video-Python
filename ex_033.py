print('Informe 3 números e vou te mostrar o Maior e o Menor entre eles')
n1 = float(input('Informe o 1º número: '))
n2 = float(input('Informe o 2º número: '))
n3 = float(input('Informe o 3º número: '))
if n1 > n2 and n1 > n3 and n2 > n3:
    maior = n1
    menor = n3
if n1 > n2 and n1 > n3 and n2 < n3:
    maior = n1
    menor = n2
if n1 > n2 and n1 < n3:
    maior = n3
    menor = n2
if n1 < n2 and n2 < n3:
    maior = n3
    menor = n1
if n2 > n1 and n2 > n3 and n1 > n3:
    maior = n2
    menor = n3
if n2 > n1 and n2 > n3 and n1 < n3:
    maior = n2
    menor = n1
print('O maior número entre os 3 informados é o número {:.1f} e o menor é {:.1f}'.format(maior, menor))

''' Esta é outra maneira de resolver o peroblema
a = float(input('1º Valor : '))
b = float(input('2º Valor: '))
c = float(input('3º Valor: '))
# Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é o maior
maior = a
if b > a and b > c:
    b = maior
if c > a and c > b:
    c = maior
print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))'''




