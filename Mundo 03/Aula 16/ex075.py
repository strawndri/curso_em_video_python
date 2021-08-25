# Aula 16

# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#
# Quantas vezes aparaceu o valor 9
# Em que posição foi digitado o primeiro valor 3
# Quais foram os números pares.

numeros = ()
pares = 0

for item in range(0,4):
  valor = int(input('Digite um número: '))
  numeros += (valor, )

print('Números:', end=' ')
for item in numeros:
  print(item, end=', ')

  if (item % 2 == 0):
    pares += 1

print(f'\nO número 9 apareceu {numeros.count(9)} vezes.')
print(f'O número 3 apareceu, pela primeira vez, na {numeros.index(3)+1}° posição' if 3 in numeros else f'O número 3 não apareceu nenhuma vez. ')
print(f'Houveram {pares} números pares.')