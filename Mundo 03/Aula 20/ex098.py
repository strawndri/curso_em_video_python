# Aula 20


# Faça um programa que tenha uma função chamda contador(), que
# receba três parâmetros: início, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:

# De 1 até 10 (1 em 1)
# De 10 até 0 (2 em 2)
# Uma contagem personalizada

from time import sleep


def contador(inicio, fim, passo):
    print('~-' * 20)
    print(f'Contagem de {inicio} até {fim}, indo de {passo} em {passo}')

    if (inicio > fim and passo > 0):
        passo *= -1

    if (passo == 0):
        passo = 1

    if (fim > 0):
        extra = 1
    else:
        extra = -1

    for item in range(inicio, fim + extra, passo):
        print(item, end=' ')
        sleep(0.5)
    print('[Fim]')


contador(1, 10, 1)
contador(10, 0, 2)

print('~-' * 20)
print('Agora é a sua vez!')

while True:
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))

    contador(inicio, fim, passo)

    opcao = input('Deseja continuar? [S/N] ').upper()
    print('--' * 20)

    if (opcao == 'N'):
        break