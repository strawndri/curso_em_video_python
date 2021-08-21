# Aula 21

# Faça um mini-sistema que utilize o interactive Help do Python. O usuário vai digitar o comando
# e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. OBS: Use cores

from time import sleep

colors = {'none': '\033[01;m',
          'white': '\033[07m \033[01m',
          'purple': '\033[01;30;45m',
          'blue': '\033[01;30;44m',
          'red': '\033[01;30;41m'}

def texto(text, color, line=False):


    if (line == True):

        largura = len(text) + 4

        print(f'{color} {"~" * largura}')
        print(f' {text:^{largura}}')
        print(f' {"~" * largura}')
        print(f'{colors["none"]}')


def ajuda():

    while True:
        texto('Sistema de Ajuda [PyHELP]', colors['purple'], line=True)
        resposta = (input(f'Função ou Biblioteca: ').lower() )

        if (resposta == 'fim'):
            texto('[Fim da Execução]', colors['purple'], line=True)
            break

        texto(f'Procurando por {resposta}...', colors["blue"], line=True)
        sleep(1)


        print(f'{colors["white"]}')
        help(resposta)
        print(f'{colors["none"]}')


ajuda()