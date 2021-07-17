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
cont50 = cont20 = cont10 = cont1 = 0

while (True):

  while (valor >= 50):
    valor -= 50
    cont50 += 1
  while (valor >= 20):
    valor -= 20
    cont20 += 1
  while (valor >=10):
    valor -= 10
    cont10 += 1
  while (valor >= 1):
    valor -= 1
    cont1 += 1

  if (valor == 0):
    print('*-' * 15)
    print('Finalizando o saque...')
    sleep(1)
    print('[Processamento finalizado com sucesso]')
    break
print(f'''Total:
{cont50} cédulas de R$50
{cont20} cédulas de R$20
{cont10} cédulas de R$10
{cont1} cédulas de R$1''')
print('*-' * 15)