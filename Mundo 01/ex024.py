# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

cidade = input('Digite o nome de uma cidade: ').strip()

if 'Santo' in cidade.split()[0].capitalize():
  print('Há "Santo" no nome desta cidade!')
else:
  print('Não há "Santo" no nome desta cidade!')

