print('Analisando Triângulos')
a = float(input('Informe o tamanho do lado A: '))
b = float(input('Informe o tamanho do lado B: '))
c = float(input('Informe o tamanho do lado C: '))
if (a < b + c) and (b < a + c) and (c < a + b):
    print('Estas medidas formam um triangulo')
    if a == b == c:
        print('Este é um triângulo do tipo Equilátero')
    elif a != b != c:
        print('Este é um triânguilo do tipo Escaleno')
    else:
        print('Este é um triângulo do tipo Isósceles')
else:
    print('Essas medidas não formam um triângulo')



