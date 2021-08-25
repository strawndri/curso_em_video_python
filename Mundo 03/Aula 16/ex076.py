# Aula 16

# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.

# No final, mostre uma listagem de preços organizando os dados em forma tabular.

produtos = ('Livro', 25.90, 'Caneta', 4.00, 'Penal', 1.50, 'Régua', 10.25)
valor = 0

print('=-' * 20)
print(f'{"Mercado Moranguinho":^40}')
print('=-' * 20)

for item in range(0, len(produtos), 2):
  print(f'{produtos[item]:.<30}', end='R$ ')
  print(f'{produtos[item + 1]:>5.2f}')
  valor += produtos[item + 1]

print('-' * 40)
print(f'{f"Total da Compra = {valor:.2f}":^40}')
print('=-' * 20)
print(f'{"Volte Sempre":^40}')
print('=-' * 20)