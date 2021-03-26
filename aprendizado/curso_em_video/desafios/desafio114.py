# Crie um código em Python que teste se o site pudim está acessível pelo
# computador usado.

import urllib.request

try:
    site = urllib.request.urlopen("http://pudim.com.br/")
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site "PUDIM" com sucesso!')
    print(site.read())  # método para fazer o python ler todo o conteúdo HTML
