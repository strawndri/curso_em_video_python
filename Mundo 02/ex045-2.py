# Aula

# Crie um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep

jokenpo = {
    'pedra_papel' : 'Papel embrulha pedra!',
    'pedra_tesoura': 'Pedra quebra tesoura!',
    'papel_tesoura': 'Tesoura corta papel!',
    'igualdade': 'Empate!'}

cores = {0: '\033[m',
         1: '\033[1;31m',
         2: '\033[1;35m',
         3: '\033[1;36m'}

print(cores[1],'*' * 40)
print('               Jokenpô              ')
print('*' * 40)

jogador = input('Você quer pedra, papel ou tesoura?  ').strip().lower()
computador = random.choice(['pedra', 'papel', 'tesoura'])

sleep(0.5)
print(cores[0], 'JO...')
sleep(0.5)
print(cores[2], 'KEN...')
sleep(0.5)
print(cores[3], 'PÔ!')
sleep(1)

print(f'{cores[0]}Jogador escolheu {cores[1]} {jogador} {cores[0]} e computador {cores[1]} {computador} {cores[0]}.')

if ((jogador == 'pedra' and computador == 'papel') or (jogador == 'papel' and computador == 'pedra')):
  print(jokenpo['pedra_papel'])
elif ((jogador == 'pedra' and computador == 'tesoura') or (jogador == 'tesoura' and computador == 'pedra')):
  print(jokenpo['pedra_tesoura'])
elif ((jogador == 'papel' and computador == 'tesoura') or (jogador == 'tesoura' and computador == 'papel')):
  print(jokenpo['papel_tesoura'])
else:
  print(jokenpo['igualdade'])

print(cores[1],'*' * 40)
print('             Fim de Jogo            ')
print('*' * 40)