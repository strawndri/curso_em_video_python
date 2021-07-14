# Aula 13

# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número: '))
contador = 0

for item in range(1, numero+1):
  if (numero % item == 0):
    contador += 1
if (contador > 2):
  print(f'{numero} não é um número primo.')
else:
  print(f'{numero} é um número primo.')