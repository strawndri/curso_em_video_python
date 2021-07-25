# Aula 17

# Faça um programa que leia 5 valores numéricos e guarde=os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

numeros = []
maior = menor = 0

for item in range(1, 6):
  numeros.append(int(input(f'{item}° valor: ')))

print(f'Sua lista: {numeros}')

# menor numero -----------------------
print(f'''Menor valor: {min(numeros)}
Posições: ''', end='')

for posicao, item in enumerate(numeros):

  if (item == min(numeros)):
    print(posicao, end='; ')

# maior número -----------------------
print(f'''\nMaior valor: {max(numeros)}
Posições: ''', end='')

for posicao, item in enumerate(numeros):

  if (item == max(numeros)):
    print(posicao, end='; ')
