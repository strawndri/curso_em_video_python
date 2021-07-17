# Aula 15

# Faça um programa que jogue par ou ímpar com o computador. O jogo só será
# interrompido quando o jogador perder, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep

vitorias = 0

print('*-' * 15)
print('PAR OU ÍMPAR')
print('*-' * 15)

while (True):
  jogador = int(input('Escolha um número: '))
  tipo = ''
  computador = randint(0, 1000)
  soma = jogador + computador
  sleep(1)

  while (opcao not in ('PpIi')):
    opcao = input('Par ou Ímpar? [P/I] ')

  print(f'''O jogador escolheu {jogador} e o computador {computador}
  A soma dos valores é {soma}.''', end='')

  if ((opcao in 'Pp') and (soma % 2 == 0)):
    print('[PAR]')
    print('Vamor continuar...')
    print('-' * 20)
  elif ((opcao in 'Ii') and (soma % 2 == 1)):
    print('[ÍMPAR]')
    print('Vamor continuar...')
    print('-' * 20)
  else:
    print('[ÍMPAR]')
    break

  vitorias += 1

print('*-' * 15)
print('GAME OVER')
print(f'Total de vitórias: {vitorias}')
print('*-' * 15)
