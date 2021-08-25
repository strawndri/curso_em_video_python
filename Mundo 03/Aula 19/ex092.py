# Aula 19

# Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastres-os (com a idade)
# em um dicionário se por acaso o CTPS for diferente de zero, o dicionário receberá também o ano de contratação
# e o salário. Calcule e acrecsente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

ano_atual = date.today().year
usuario = {}

while True:
  usuario['Nome'] = input('Nome: ')
  nascimento = int(input('Ano de Nascimento: '))
  usuario['Idade'] = ano_atual - nascimento
  usuario['CTPS'] = int(input('Carteira de Trabalho (0 caso não tenha): '))

  if (usuario['CTPS'] == 0):
    break
  else:
    usuario['Ano de Contratação'] = int(input('Ano de contratação: '))
    usuario['Salário'] = float(input('Salário atual:'))

    usuario['Aposentadoria'] = (35 - (ano_atual - usuario['Ano de Contratação']) ) + usuario['Idade']

    if (len(usuario) == 6):
      break

print('*-' * 15)
for key, value in usuario.items():
  print(f'{key}: {value}')

