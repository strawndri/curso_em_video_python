# Aula 19

# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em ordem, sabendo que o vencedor tirou o
# maior número no dado.

# Versão 2

from random import randint
from time import sleep
from operator import itemgetter

print('*-' * 16)
print(f'{"Jogo de Dados":^32}')
print('*-' * 16)

jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}

for key, value in jogo.items():
  print(f'O {key} tirou o valor {value} no dado.')
  sleep(1)

ranking = []
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('*-' * 16)
print(f'{"RANKING":^32}')
print('*-' * 16)

for item, value in enumerate(ranking):
  print(f'{item + 1}° Lugar: {value[0]} com {value[1]}')
  sleep(1)



