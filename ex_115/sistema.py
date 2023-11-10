from time import sleep

from ex_115.Lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair Do Sistema'])
    if resposta == 1:
        # Opção de listar o conteudo de um arquivo.
        lerarquivo(arq)
    elif resposta == 2:
        # Opção para cadastrar uma nossa pessoa
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        sleep(1)
        cabeçalho('Saindo do sistema...Até logo!')
        break
    else:
        print('\033[31mErro! Digite Uma Opção Válida!\033[m')
    sleep(1)
