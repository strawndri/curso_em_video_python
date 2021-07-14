# Aula 13

# Desenvolva um programa que leia seis números inteiros e mostre a
# soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
for item in range(0, 6):
  numero = int(input(f'{item + 1}° Número: '))
  if (numero % 2 == 0):
    soma += numero
print(f'Soma dos números pares: {soma}')