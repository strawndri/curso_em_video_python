# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

import math

numero = float(input('Digite um número: '))
n_inteiro = math.trunc(numero)
print(f'A porção inteira do seu número é {n_inteiro}')