from datetime import datetime


def voto(analise):
    ''' Função para analizar se o usuário está qualificado para votação
    levando em consideração sua data de nascimento
    :param analise: data de nascimento do usuário.
    :return: cond = resultado da análise. '''

    nasc = analise
    idade = datetime.today().year - nasc
    if (idade >= 16) and (idade < 18) or (idade >= 65):
        cond = f'Com {idade} anos o voto é opcional'
        return cond
    elif idade < 16:
        cond = f' Com {idade} anos ainda não pode votar'
        return cond
    else:
        cond = f' Com {idade} anos o voto é obrigatório'
        return cond


nasc = int(input('Informe seu ano de nascimento: '))
voto(nasc)
print(voto(nasc))
