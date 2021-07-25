# Aula 17

# Crie um programa que o usuário possa digitar cinco valores
# numéricos e cadastre-os em uma lista, já na posição correta da
# inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

numeros = []
for item in range(0, 5):
  valor = int(input('Digite um valor: '))

  if (item == 0 or valor >= max(numeros)):
    numeros.append(valor)
  else:
    for num in range(0, len(numeros)):
      if (valor not in numeros):
        if (valor < numeros[num]):
          numeros.insert(num, valor)

print(f'Lista em ordem crescente: {numeros}')