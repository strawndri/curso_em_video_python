cores = {'normal': '\033[01;m',
         'vermelho': '\033[01;31m',
         'amarelo': '\033[01;33m',
         'roxo': '\033[01;35m'}


def formatar(texto, cor=cores['normal'], linha=False):
    if (linha == True):

        print(f'{cores["normal"]}-' * 50)
        print(f'{cores[cor]}{texto}{cores["normal"]}'.center(60))
        print(f'{cores["normal"]}-' * 50)
    else:
        print(f'{cores[cor]} {texto} {cores["normal"]}')