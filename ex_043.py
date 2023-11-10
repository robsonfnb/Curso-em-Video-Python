print('Cálculo de IMC')
p = float(input('Informe seu peso em Kg: '))
a = float(input('Informe sua altura em metros: '))
imc = p / (a * a)
if imc < 18.5:
    print('Seu IMC é {:.1f}.Você está abaixo do seu peso ideal'.format(imc))
elif imc >= 18.5 and imc < 25:
    print(' Seu IMC é {:.1f}. Você está na faixa de peso ideal'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.1f}. Você está com sobrepeso'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é {:.1f}. Você está na faixa de obesidade'.format(imc))
elif imc >40:
    print('Seu IMC é {:.1f}. Você está na faixa de obesidade mórbida'.format(imc))

