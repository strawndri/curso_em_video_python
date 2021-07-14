# Aula 13

# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

n1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for item in range(0, 10):
  n = 0
  n = (n1 + (n1 - 1)) * razao
  print(n1, end=" ")
  n1 += razao