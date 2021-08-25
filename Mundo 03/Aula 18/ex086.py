# Aula 18

# Faça um programa que crie uma matriz de dimensão 3x3 e preencha
# com valores lidos pelos teclado. No final, mostre a matriz na tela,
# com a formatação correta.

matriz = [[], [], []]

for row in range(0, 3):
  for column in range(0, 3):
    valor = int(input((f'Digite um valor para {(row, column)}: ')))
    matriz[row].append(valor)

for row in range(0, 3):
  for item in matriz[row]:
    print(f'[{item}]', end='')
  print(end='\n')