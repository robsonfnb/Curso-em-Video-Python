def notas(*n, sit=False):
    """
    -> Função que recebe notas de alunos e exibe a situação de acordo com a média das notas.
    :param n: recebe as notas do aluno (quantas forem necessarias)
    :param sit: opcional(exibe a situação do aluno de acordo com a médias das notas)
    :return: Informações de acordo com as notas informadas.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'REGULAR'
        else:
            r['situacao'] = 'RUIM'
    return r


# Programa principal
resp = notas(10, 5, 5.5, sit=True)
print(resp)
print('-' * 100)
help(notas)
