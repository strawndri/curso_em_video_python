# Aula

# Crie um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep

print('*' * 40)
print('               Jokenpô              ')
print('*' * 40)

jogador = input('''Você quer PEDRA, PAPEL ou TESOURA?
''').strip().lower()
computador = random.choice(['pedra', 'papel', 'tesoura'])

sleep(0.5)
print('JO...')
sleep(0.5)
print('KEN...')
sleep(0.5)
print('PÔ!')

print('*' * 40)
print(f'Jogador escolheu {jogador} e computador {computador}.')

if ((jogador == 'pedra' and computador == 'papel') or (jogador == 'papel' and computador == 'pedra')):
  print('Papel embrulha pedra!')
elif ((jogador == 'pedra' and computador == 'tesoura') or (jogador == 'tesoura' and computador == 'pedra')):
  print('Pedra quebra tesoura!')
elif ((jogador == 'papel' and computador == 'tesoura') or (jogador == 'tesoura' and computador == 'papel')):
  print('Tesoura corta papel!')
else:
  print('Empate!')

print('*' * 40)
print('             Fim de Jogo            ')
print('*' * 40)