# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre
# uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite.

velocidade = float(input('Velocidade, em quilômetros por hora, a qual você esta dirigindo: '))
print('~' * 80)

if velocidade > 80:
  multa = (velocidade - 80) * 7.00
  print(f'Você foi multado(a) por infrigir as leis de trânsito, visto que ultrapassou o limite de 80Km/h.')
  print(f'Sua multa será de: R$ {multa:.2f}.')
elif velocidade == 80:
  print(f'Cuidado! Você está no limite de velocidade.')
else:
  print(f'Você está com a velocidade normal.')