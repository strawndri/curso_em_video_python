# Aula 20

# Faça um programa que tenha uma lista chamada números e duas
# funções chamadas sorteia() e somaPar(). A primeira função vai
# sortear 5 números e vai colocá-los dentro da lista e a segunda
# função vai mostrar a soma entre todos os valores pares sorteados
# pela função anterior.

from random import randint
from time import sleep

numeros = []

def sorteia():

  print(f'Os números sorteados são:', end=' ')
  for item in range(0, 5):
    valor = randint(1, 10)

    print(valor, end= ' ')
    sleep(0.5)

    numeros.append(valor)
  print()

def somaPar(lista):
  soma = 0
  for item in lista:

    if (item % 2 == 0):
      soma += item

  print(f'A soma de todos os números pares é {soma}!')

sorteia()
somaPar(numeros)
