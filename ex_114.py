import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site não se encontra acessível no momento')
else:
    print('O site foi acessado com sucesso')
    print('Aqui embaixo está o código da página')
    print(site.read())
