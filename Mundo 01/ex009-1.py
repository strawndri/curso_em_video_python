# Faça um programa que leia um número qualquer e mostre na tela sua tabuada.

valor = int(input('Digite um número: '))
n = 0

print(f'A Tabuada de {valor} é:')

while n <= 10:
  print(f'{valor} X {n} = {valor * n} \n')
  n = n + 1