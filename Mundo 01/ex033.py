# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

if n1 > n2 and n1 > n3:
  print(f'{n1} é o maior número entre os outros.')
elif n2 > n1 and n2 > n3:
  print(f'{n2} é o maior número entre os outros.')
else:
   print(f'{n3} é o maior número entre os outros.')

if n1 < n2 and n1 < n3:
  print(f'{n1} é o menor número entre os outros.')
elif n2 < n1 and n2 < n3:
  print(f'{n2} é o menor número entre os outros.')
else:
   print(f'{n3} é o menor número entre os outros.')


