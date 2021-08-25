# Aula 18

# Faça um programa que leia o nome e o peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

# a) Quantas pessoas foram cadastradas;
# b) Uma listagem com as pessoas mais pesadas;
# c) Uma listagem com as pessoas mais leves;

grupo = []
pessoa = []
peso = []
pesados = []
leves = []
opcao = ''

while True:
  pessoa.append(input('Nome: '))
  peso.append(float(input('Peso (Kg): ')))
  opcao = input('Deseja Continuar? [S/N] ').upper()

  if (opcao == 'N'):
    break

grupo.append(pessoa[:])
grupo.append(peso[:])

for key, item in enumerate(grupo[1]):

  if (item == max(grupo[1])):
    pesados.append(grupo[0][key])
  elif (item == min(grupo[1])):
    leves.append(grupo[0][key])

print('*-' * 15)
print(f'''Foram registradas {len(grupo[0])} pessoas
Pessoas mais pesadas ({max(grupo[1])} Kg): {pesados}
Pessoas mais leves ({min(grupo[1])} Kg): {leves}''')


