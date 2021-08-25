# Aula 19

# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quanta partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos
# durante o campeonato.

jogador = {}

jogador['Nome'] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
gols = list()
total_gols = 0

for item in range(0, partidas):
  quantidade_gols = int(input(f'Gols na {item + 1}° partida: '))
  gols.append(quantidade_gols)

  total_gols += quantidade_gols


jogador['Gols'] = gols
jogador['Total'] = total_gols

print('-~-' * 15)
print(jogador)
print('-~-' * 15)


print('-~-' * 15)
for key, value in jogador.items():
  print(f'O campo {key} tem valor igual a {value}')
print('-~-' * 15)

print('-~-' * 15)

for key, value in jogador.items():

  if (key == 'Nome'):
    print(f'{value} realizou {partidas} partidas!')
  elif (key == 'Gols'):
    for i, item in enumerate(value):
      print(f'  Na {i + 1}° partida foram {item} gols')
  else:
    print(f'Total de gols: {value}')
print('-~-' * 15)

