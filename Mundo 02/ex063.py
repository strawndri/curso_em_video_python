# Aula 14

# Escreva um programa que leia um número "n" inteiro qualquer e mostre
# na telas os "n" primeiros elementos de uma Sequência de Fibonacci

n = int(input('Quantos valores? '))
termo_1 = 0
termo_2 = 1
termo_3 = 0
contador = 3

print(f'{termo_1} - {termo_2}', end='')

while (contador <= n):
  termo_3 = termo_1 + termo_2
  print(f' - {termo_3}', end='')

  termo_1 = termo_2
  termo_2 = termo_3

  contador += 1
print(' [Fim]')
