# Aula 15

# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.

# OBS: Considere que o caixa possui cédulas de 50, 20, 10 e 1.

from time import sleep

print('*-' * 15)
print('Caixa Eletrônico da Andrieli')
print('*-' * 15)
valor = int(input('Quantos reais você deseja sacar? R$ '))
total = valor
cedula = 50
total_cedulas = 0

while (True):

  if (total >= cedula):
    total -= cedula
    total_cedulas += 1
  else:
    if (total_cedulas > 0):
      print(f'{total_cedulas} cédulas de {cedula}')

    if (cedula == 50):
      cedula = 20
    elif (cedula == 20):
      cedula = 10
    elif (cedula == 10):
      cedula = 1
    total_cedulas = 0

    if (total == 0):
      print('*-' * 15)
      print('Finalizando o saque...')
      sleep(1)
      print('[Processamento finalizado com sucesso]')
      break
