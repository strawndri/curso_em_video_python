#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco_antigo = float(input('Digite um preço antigo do produto: R$ '))
preco_novo = preco_antigo - (preco_antigo * 0.05)

print(f'O preço novo do produto, após 5% de desconto, é: R$ {preco_novo:.2f}.')

