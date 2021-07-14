# Aula 14

# Crie um porgrama que leia dois valores e mostre um menu na tela:

# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

# cores -----------------------------------

cores = {
    0 : '\033[m',
    1 : '\033[1;33m',
    2 : '\033[1;35m',
}

# variáveis -------------------------------
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opcao = 0
resultado = 0

itens = {
    1 : 'Somar números',
    2 : 'Multiplicar Números',
    3 : 'Maior número',
    4 : 'Novos Números',
    5 : 'Sair do Programa'
}

# processamento ----------------------------

while (opcao != 5):
  print(f'{cores[2]}*-' * 15)
  opcao = int(input(f'''{cores[1]}Selecione uma das opções abaixo:
  [1]: Somar
  [2]: Multiplicar
  [3]: Maior
  [4]: Novos números
  [5]: Sair do programa
  {cores[0]}'''))
  print(f'[{opcao}] {itens[opcao]}')

  if (opcao == 1):
    resultado = n1 + n2
    print(f'Resultado: {resultado}')
  elif (opcao == 2):
    resultado = n1 * n2
    print(f'Resultado: {resultado}')
  elif (opcao == 3):
    if (n1 > n2):
      print(f'Resultado: {n1} é maior que {n2}.')
    elif (n1 < n2):
      print(f'Resultado: {n2} é maior que {n1}.')
    else:
      print(f'Resultado: {n1} e {n2} são iguais.')
  elif (opcao == 4):
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
