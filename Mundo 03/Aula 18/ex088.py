# Aula 18

# Faça um programa que ajude um jogador na MEGA SENA a criar palpites. O programa vai
# perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60, para cada
# jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

print('°' * 40)
print(f'{"MEGA SENA":^40}')
print('°' * 40)
quantidade = int(input('Quantos jogos você deseja realizar? '))
print('-' * 40)

palpites = []
jogo = []

for item in range(0, quantidade):
  contador = 0

  while (contador < 6):
    n = randint(1, 60)

    if (n not in jogo):
      jogo.append(n)
      contador += 1

  jogo.sort()
  palpites.append(jogo[:])
  jogo.clear()


for key, item in enumerate(palpites):
  sleep(1)
  print(f'{key + 1}° Jogo: {item}')

print('-' * 40)