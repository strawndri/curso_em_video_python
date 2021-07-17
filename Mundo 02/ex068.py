# Aula 15

# Faça um programa que jogue par ou ímpar com o computador. O jogo só será
# interrompido quando o jogador perder, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep

cores = {
  0 : '\033[1;37m',     # sem cor
  1 : '\033[1;31m', # vermelho
  2 : '\033[1;36m', # verde
  3 : '\033[1;35m', # roxo
}
vitorias = 0

print(f'{cores[0]}')
print('*-' * 15)
print(f'{"PAR OU ÍMPAR":^30}')
print('*-' * 15)

while (True):
  jogador = int(input('Escolha um número: '))
  opcao = ' '
  computador = randint(0, 1000)
  soma = jogador + computador

  while (opcao not in ('PpIi')):
    opcao = input('Par ou Ímpar? [P/I] ')

  sleep(1)

  print(f'''O jogador escolheu {cores[3]} {jogador} {cores[0]} e o computador {cores[3]} {computador} {cores[0]}
A soma dos valores é {cores[3]} {soma} {cores[0]}.''', end='')

  print(f'{cores[2]}[PAR]{cores[0]}' if  (soma % 2 == 0) else f'{cores[1]}[ÍMPAR]{cores[0]}')

  if ((opcao in 'Pp') and (soma % 2 == 0)):
    print('Vamor continuar...')
    print('-' * 20)
  elif ((opcao in 'Ii') and (soma % 2 == 1)):
    print('Vamor continuar...')
    print('-' * 20)
  else:
    break

  vitorias += 1

print('*-' * 15)
print(f'{cores[1]}{"GAME OVER":^30}{cores[0]}')
print(f'Total de vitórias: {cores[3]} {vitorias} {cores[0]}')
print('*-' * 15)
