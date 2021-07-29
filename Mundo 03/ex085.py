# Aula 18

# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastres-os
# em uma lista única que mantenha separados os valores pares e ímpares. No final,
# mostre os valores pares e ímpares em ordem crescente.

numeros = [[], []]

for item in range(0, 7):
  valor = int(input('Digite um número: '))

  if (valor % 2 == 0):
    numeros[0].append(valor)
  else:
    numeros[1].append(valor)

numeros[0].sort()
numeros[1].sort()

print(f'''Pares: {numeros[0]} 
Impares: {numeros[1]} ''')