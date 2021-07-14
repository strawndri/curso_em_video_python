# Aula 14

# Refaça o exercício 051, lendo o primeiro termo e
# a razão de uma P.A, mostrando os 10 primeiros termos
# da progressão usando a estrutura while.

n1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
contador = 0

while (contador < 10):
  print(f'{n1}', end = ' -> ')
  n1 += razao
  contador += 1
print('Fim da Progressão Aritmética!')