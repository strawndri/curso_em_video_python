# Aula 20


# Faça um programa que tenha uma função chamda contador(), que
# receba três parâmetros: início, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:

# De 1 até 10 (1 em 1)
# De 10 até 0 (2 em 2)
# Uma contagem personalizada

from time import sleep

from time import sleep


def contador(inicio, fim, passo):
    contador = inicio

    if (passo < 0):
        passo *= -1
    elif (passo == 0):
        passo = 1

    print('~-' * 20)
    print(f'Contagem de {inicio} a {fim}, indo de {passo} em {passo}')
    sleep(0.2)

    if (inicio < fim):
        while (contador <= fim):
            print(f'{contador}', end=' ')
            sleep(0.5)
            contador += passo
    elif (inicio > fim):
        while (contador >= fim):
            print(f'{contador}', end=' ')
            sleep(0.5)
            contador -= passo
    print('[FIM]')


contador(1, 10, 1)
contador(10, 0, 2)

print('~-' * 20)
print(f'{"Agora é sua vez!":^40}\n')

while True:
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))

    contador(inicio, fim, passo)

    opcao = ' '
    while (opcao not in 'SN'):
        opcao = input('Deseja continuar? [S/N] ').upper()[0]
    print('--' * 20)

    if (opcao == 'N'):
        print(f'{"[FIM DA EXECUÇÃO]":^40}')
        break
