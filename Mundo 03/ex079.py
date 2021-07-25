# Aula 17

# Crie um programa em que o usuário possa digitar vários valores numéricos e cadastre-os
# em uma lista. Caso o numéro já exista lá dentro, ele não será adicionado. No final, serão
# exibidos todos os valores únicos digitados, em ordem crescente.

numeros = []
opcao = ''

while True:
  valor = int(input('Digite um valor: '))
  opcao = input('Deseja continuar? [S/N] ').upper()

  while (opcao not in 'SsNn'):
    opcao = input('Tente novamente. Deseja continuar? [S/N] ').upper()

  if valor not in numeros:
    numeros.append(valor)

  if (opcao == 'N'):
    break

numeros.sort()

print(f'Números em ordem crescente: {numeros}')
