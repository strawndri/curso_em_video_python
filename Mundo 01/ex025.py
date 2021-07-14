# Crie um programa que leia o nome de um pessoa e diga se ela tem "Silva" no nome.

nome = str(input('Digite o seu nome completo:')).strip()
if 'silva' in nome.lower():
  print('Há "Silva" em seu nome!')
else:
  print('Não há "Silva" em seu nome!')

