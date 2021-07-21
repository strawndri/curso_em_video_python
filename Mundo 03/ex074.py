# Aula 16

# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#
# Depois disso, mostre a listagem e números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
numeros = ()
maior = menor = 0

for item in range(0, 5):
  aleatorio = randint(1,10)
  numeros += (aleatorio,)

  if (item == 0):
    maior = menor = aleatorio
  else:
    if (aleatorio > maior):
      maior = aleatorio
    elif (aleatorio < menor):
      menor = aleatorio

print(f'''Os números aleatórios são: {numeros}
{maior} é o maior e {menor} é o menor.''')