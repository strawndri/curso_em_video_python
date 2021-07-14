# Aula

# Escreva um programa para aprovar um empréstimo de uma casa.
# O programa vai perguntar o valor da casa, do salário do comprador
# e em quantos anos ele vai pagar. Calcule o valor da prestação mensal,
# sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
anos = int(input('Em quantos anos você pagará? '))

prestacao = (valor_casa / (anos * 12))
limite = (salario * 0.30)

if prestacao > limite:
  print('Empréstimo negado.')
else:
  print(f'Empréstimo aprovado \n Valor mensal da prestação: R$ {prestacao:.2f}')