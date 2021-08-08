# Aula 20

# Faça um programa que tenha uma função chamada maior(), que recebe vários
# parâmetros com valores inteiros. Seu programa tem que analisar todos os
# valores e dizer qual deles é o maior.

from time import sleep

def maior(*numeros):
  print('+-' * 20)
  print(f'Foram informados {len(numeros)} valores!')

  for i, item in enumerate(numeros):
    sleep(0.5)
    if (i == (len(numeros) - 2) ):
      print(item, end = ' e ')
    elif ( i == (len(numeros) - 1)):
      print(item)
    else:
      print(item, end = ', ')

  if (len(numeros) == 0):
    maximo = 0
  else:
    maximo = max(numeros)

  print(f'O maior número entre todos é {maximo}!')

maior(50, 23, 100, 89, 2, 45, 109)
maior(-4, 66, 13)
maior()