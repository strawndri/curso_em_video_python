# Aula

# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base da conversão:
#
# [1] para binário
# [2] para octal
# [3] para hexadecimal

valor = int(input('Digite um número inteiro: '))
base = int(input('''Escolha sua base de conversão: 
1: Binário 
2: Octal
3: Hexadecimal
Opção escolhida: '''))

if (base == 1):
  binario = format(valor, "b")
  print(f'{valor} para Binário: {binario}')
elif (base == 2):
  octal = format(valor, "o")
  print(f'{valor} para Octal: {octal}')
elif (base == 3):
  hexadecimal = format(valor, "x")
  print(f'{valor} para Hexadecimal: {hexadecimal}')
else:
  print('Opção inválida')