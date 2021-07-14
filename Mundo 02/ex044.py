# Aula

# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

valor = float(input('Valor do produto: R$ '))

print('--' * 12)
condicao = int(input('''Com você deseja pagar?
(1): À vista dinheiro/cheque 
(2): À vista no cartão
(3): Em até 2x no cartão
(4): 3x ou mais no cartão
Digite aqui o número escolhido: '''))
print('--' * 12)

if (condicao == 1):
  total = valor - (valor * 0.10)
elif (condicao == 2):
  total = valor - (valor * 0.05)
elif (condicao == 3):
  total = valor
  parcela = total / 2
  print(f'Você pagará 2x de R$ {parcela:.2f}')
elif (condicao == 4):
  total = valor + (valor * 0.20)
  quantidade_parcelas = int(input('Em quantas parcelas você deseja pagar? '))
  parcela = total / quantidade_parcelas
  print(f'Você pagará {quantidade_parcelas}x de R$ {parcela:.2f}')
else:
  total = 0
  print('[ERRO NO PAGAMENTO]')

print(f'Valor final: {total}')