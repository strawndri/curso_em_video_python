# Aula 17

# Crie um programa que leia vários números e coloque-os em uma lista.
# Depois disso, crie duas listas extras que vão contar apenas os valores
# pares e os valores ímpares digitados, respectivamente. Ao final, mostre o
# conteúdo das três listas geradas.

opcao = ''
numeros = []
pares = []
impares = []

while True:
  n = int(input('Digite um número: '))
  opcao = input('Deseja continuar? [S/N] ').upper()

  numeros.append(n)

  if (opcao == 'N'):
    break

for item in numeros:
  if (item % 2 == 0):
    pares.append(item)
  elif (item % 2 == 1):
    impares.append(item)

print(f'{"[Fim da Execução]":-^10}')
print(f'''
Lista inicial: {numeros}
Lista de números pares: {pares}
Lista de números ímpares: {impares}''')