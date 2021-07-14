# Aula 13

# Faça um programa que mostre uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de um resgundo entre elas.

from time import sleep

for item in range(10, -1, -1):
  print(item)
  sleep(1)
print('Feliz ano novo!!!')