# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

numero = input('Digite um número de 0 a 9999: ')
quantidade = len(numero)
contador = 0

while contador < quantidade:
  print(numero[contador])
  contador = contador + 1


