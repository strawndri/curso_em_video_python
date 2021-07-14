# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

print('~' * 30)
print('Você sabe quais anos são bissextos?')

ano = int(input('''Escreva o ano que gostaria de analisar:  
Obs: Para o ano atual, digite 0. '''))
print('~' * 30)

if ano == 0:
  ano = date.today().year

if ((ano % 4 ) == 0) and ((ano % 100) != 0) or ((ano % 400) == 0):
  print(f'{ano} é um ano bissexto.')
else:
  print(f'{ano} não é um ano bissexto.')

