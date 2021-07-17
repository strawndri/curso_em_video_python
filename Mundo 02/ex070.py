# Aula 15

# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final, mostre:

# Qual é o total gasto na compra
# Quantos produtos custam mais de R$1000,00
# qual é o nome do produto mais barato.

total = contador = contador_preco = menor = 0
nome_barato = ''

while (True):

  nome = input('Nome do produto: ')
  preco = float(input('Preço: R$ '))
  opcao = ' '

  while (opcao not in 'SN'):
    opcao = input('Deseja continuar [S/N]: ').strip().upper()[0]

  total += preco
  contador += 1

  if (preco > 1000):
    contador_preco += 1

  if (contador == 1):
    menor = preco
    nome_barato = nome
  else:
    if (preco < menor):
      menor = preco
      nome_barato = nome


  if (opcao in 'N'):
    print(f'{"FIM DO PROGRAMA":^20}')
    print('*-' * 15)
    break

print(f'''
Você comprou {contador} produtos
Total da compra: R$ {total}
Houveram {contador_preco} produtos que custaram mais de R$1000,00
{nome_barato} foi o produto mais barato''')