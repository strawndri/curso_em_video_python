#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

dinheiro = float(input('Digite a quantidade de dinheiro que você possui em  sua carteira: R$ '))
dolar = dinheiro / 5.22

print(f'Você pode comprar {dolar:.2f} dólares.')

