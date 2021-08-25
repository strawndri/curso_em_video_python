# Aula 21

# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetros o ano de
# nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO,
# OPCIONAL ou OBRIGATÓRIO nas eleições.

def voto(data):
  from datetime import date
  ano_atual = date.today().year

  idade = (ano_atual - data)

  if (idade < 18):
    resultado = '[NEGADO] -- Você não pode votar.'
  elif (16 >= idade < 18 and idade >= 65):
    resultado = '[OPCIONAL] -- Você pode optar em votar ou não.'
  else:
    resultado = '[OBRIGATÓRIO] -- Você deve votar.'

  return print(resultado)


nascimento = int(input('Ano de nascimento: '))
voto(nascimento)