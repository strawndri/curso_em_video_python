# Aula

# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com sua idade. Seu programa também deverá mostrar o tempo
# que falta ou que passou do prazo.

# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo de alistamento

from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Digite seu ano de nascimento: '))
idade = ano_atual - ano_nascimento

print(f'''Você nasceu em: {ano_nascimento}
Idade em {ano_atual}: {idade} anos.''')

if (idade < 18):
  tempo = 18 - idade
  print(f'Logo, ainda se alistará. Seu tempo até lá é de {tempo} anos.')
elif (idade > 18):
  tempo = idade - 18
  print(f'Logo, passou {tempo} anos do alistamento.')
else:
  print('Logo, está na hora de se alistar ao serviço militar!')