# Escreva um programa que faça o computador "pensar" em um número
# inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
# foi o número escolhido pelo computador. O programa deverá escrever
# na tela se o usuário venceu ou perdeu.

from random import randrange
from time import sleep
n_aleatorio = randrange(0,5)

amarelo = '\033[1;33m'
sem_cor = '\033[m'

n_resposta = int(input(f'{amarelo}Tente descobrir o número escolhido pelo computador. Digite um valor entre 0 e 5: '))
print(f'{amarelo}~' * 82)
print(f'{amarelo} Carregando...')
sleep(1)

if n_resposta == n_aleatorio:
  print(f'{amarelo}Parabéns, você acertou! O número era {n_aleatorio}.')
else:
  print(f'{amarelo}Que pena, você errou! O número escolhido foi {n_aleatorio}.')