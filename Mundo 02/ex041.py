# Aula

# A Confederação Nacional de Natação precisa de um programa que leia o ano de
# nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 25 anos: Sênior
# Acima: Master

from datetime import date

print('~~' * 5, 'Confederação Nacional de Natação', '~~' * 5)
print('~~~' * 18)

ano_atual = date.today().year
nascimento = int(input('Digite sua data de nascimento: '))
idade = ano_atual - nascimento

print(f'Idade: {idade} anos.')

if (idade <= 9):
  print('Você é Mirim.')
elif (idade <= 14):
  print('Você é Infantil.')
elif (idade <= 19):
  print('Você é Junior.')
elif (idade == 25):
  print('Você é Sênior.')
else:
  print('Você é Master.')