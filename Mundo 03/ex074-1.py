# Aula 16

# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#
# Depois disso, mostre a listagem e números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print('Números aleatórios: ', end='')
for item in numeros:
  print(item, end=' ')

print(f'''\nO maior número foi: {max(numeros)}
O menor número foi: {min(numeros)}''')