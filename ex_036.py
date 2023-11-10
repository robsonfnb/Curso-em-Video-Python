print('Empréstimo bancário para compra de imóvel')
print('O emprestimo só será aprovado se a parcela não ultrapassar 30% do valor do seu salário')
nome = str(input('Informe o seu nome: '))
sal = float(input('Informe o seu salário: R$'))
valor = float(input('Qual é o valor do imóvel que você pretende adquirir? R$'))
anos = int(input('Em quantos anos pretende quitar o imóvel? :'))
parcela = valor / (anos * 12)
if parcela <= sal * 30 / 100:
    print('{} seu empréstimo será aprovado'.format(nome.title()))
    print('Você ira pagar uma parcela de R${:.2f} por {} anos para poder quitar o imóvel no valor de R${:.2f} '.format(parcela, anos,valor))
else:
    print('{} sinto muito, seu emprestimo não será aprovado'.format(nome.title()))
    print('A parcela de R${:.2f} ultrapassa os 30% do valor total do seu salário'.format(parcela))

