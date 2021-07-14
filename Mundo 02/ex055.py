# Aula 13

# Faça um porgrama que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for item in range(1, 6):
  peso = float(input(f'{item}° peso: '))

  if (item == 1):
    maior = peso
    menor = peso
  else:
    if (peso > maior):
      maior = peso
    elif (peso < menor):
      menor = peso

print(f'''Maior peso: {maior}
Menor peso: {menor}''')