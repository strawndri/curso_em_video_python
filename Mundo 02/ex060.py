# Aula 14

# Faça um programa que leia um número qualquer e mostre seu fatorial.

numero = int(input('Digite um número: '))
contador = numero
fatorial = 1

print(f'{numero}! = ', end='')

while (contador > 0):
  print(f'{contador}', end='')
  print(' x ' if contador > 1 else ' = ', end='')
  fatorial *= contador
  contador -= 1
print(f'[{fatorial}]')