# Aula 19

# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em ordem, sabendo que o vencedor tirou o
# maior número no dado.

from random import randint
jogo = {}
maior = menor = 0

for item in range(1, 5):
  jogo[f'jogador{item}'] = randint(1, 6)

for key, value in jogo.items():
  print(f'O {key} tirou {value}')
print('*-' * 15)
for i, item in enumerate(sorted(jogo, key = jogo.get, reverse=True)):
  print(f'{i + 1}° Lugar: {item} com {jogo[item]}')
