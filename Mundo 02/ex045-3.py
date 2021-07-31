# Aula

# Crie um programa que faça o computador jogar Jokenpô com você.

import random

print('*' * 40)
print('               Jokenpô              ')
print('*' * 40)

jogador = input('Você quer pedra, papel ou tesoura?  ').strip().lower()
computador = random.choice(['pedra', 'papel', 'tesoura'])

print(f'Jogador escolheu {jogador} e computador {computador}.')

if (jogador == 'pedra'):
  if (computador == 'papel'):
    print('Papel embrulha pedra!')
  elif (computador == 'tesoura'):
    print('Pedra quebra tesoura!')
  else:
    print('Empate!')
elif (jogador == 'papel'):
  if (computador == 'pedra'):
    print('Papel embrulha pedra!')
  elif (computador == 'tesoura'):
    print('Tesoura corta papel!')
  else:
    print('Empate!')
elif (jogador == 'tesoura'):
  if (computador == 'pedra'):
    print('Pedra que tesoura!')
  elif (computador == 'papel'):
    print('Tesoura corta papel!')
  else:
    print('Empate')

print('*' * 40)
print('             Fim de Jogo            ')
print('*' * 40)