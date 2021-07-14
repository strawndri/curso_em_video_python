# Aula 13

# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não antigiram a maioridade e quantas já são maiores.

from datetime import date

maior_idade = 0
menor_idade = 0

for item in range(0, 7):
  nascimento = int(input(f'{item+1}° Data de Nascimento: '))
  idade = date.today().year - nascimento

  if (idade >= 18):
    maior_idade += 1
  else:
    menor_idade += 1

print(f'''Pessoas maior de idade: {maior_idade}
Pessoas menor de idade: {menor_idade}''')