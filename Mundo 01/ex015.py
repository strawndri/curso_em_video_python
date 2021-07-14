# Escreva um programa que pergunte a quantidade Km percorridas por um carro
# alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço
# a pagar, sabendo que o carro custa RS60 por dia e R$0.15 por Km rodado.

km = float(input('Quantos quilômetros você percorreu com o carro alugado? '))
dias = int(input('Quantos dias você o alugou? '))
preco = (km * 0.15) + (dias * 60)

print(f'Após ficar {dias} dias com o carro e percorrer {km}km, você deve pagar R$ {preco:.2f}.')
