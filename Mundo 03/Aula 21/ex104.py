# Aula 21

# Crie um programa que tenha a função leiaInt(),
# que vai funcionar de forma semelhante à função input()
# do Python, só que fazendo a validação para aceitar apenas
# um valor numérico.

def chamada(texto):
  print('~~' * 20)
  print(f'{texto:^40}')
  print('~~' * 20)

def leiaInt(valor):

  while True:
    valor = input('Digite um número: ')

    if (valor.isnumeric() == False):
      chamada('[ERRO] -- Digite um número inteiro!')
    else:
      return valor
      break

numero = leiaInt('Digite um número: ')
print(f'O número escolhido foi {numero}!')

