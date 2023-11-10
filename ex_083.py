print('De acordo com a quantidade de parenteses abertos e fechados iremos analisar se é ou não uma expressão válida')
exp = (str(input('Digite uma expressão: ')))
formula = list()
for simb in exp:
    if simb == '(':
        formula.append('(')
    elif simb == ')':
        if len(formula) > 0:
            formula.pop()
        else:
            formula.append(')')
            break
if len(formula) == 0:
    print('Essa é uma expressão válida.')
else:
    print('Essa é uma expressão inválida')
print(formula)
