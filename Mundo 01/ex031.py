# Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem, cobrando R$0,50
# por Km para viagens de até 200Km e RS0,45 para viagens mais longas.


distancia = float(input('Qual é o tamanho, em quilômetros, da distância? '))

if distancia <= 200:
  preco_passagem = distancia * 0.5
  print(f'O preço da passagem será: R$ {preco_passagem:.2f}')
else:
  preco_passagem = distancia * 0.45
  print(f'O preço da passagem será: R$ {preco_passagem:.2f}')

