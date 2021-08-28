# Aula 23

# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado

import urllib.request

url = 'http://www.pudim.com.br/'

try:
    urllib.request.urlopen(url)
except urllib.error.URLError:
    print('\033[01;31m O site PUDIM não está funcionando agora!\033[m')
else:
    print('\033[01;36m O site PUDIM está funcionando agora!\033[m')