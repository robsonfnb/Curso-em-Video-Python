def calculaarea():
    a = c * l
    return a


c = float(input('informe o comprimento em metros: '))
l = float(input('informe a largura em metros: '))
print(f'A área de um terreno {c:.2f} m x {l:.2f} m resulta em {calculaarea()} metros²')


