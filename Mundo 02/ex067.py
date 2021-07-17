# Aula 15

# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while (True):
  n = int(input('Digite um número: '))

  if (n < 0):
    print('''[FIM DA EXECUÇÃO]''')
    break

  print('*-' * 10)
  print(f'TABUADA DO NÚMERO {n}')
  print('-' * 20)

  for item in range(0,11):
    resultado = n * item
    print(f'{n} x {item} = {resultado}')
  print('*-' * 10)