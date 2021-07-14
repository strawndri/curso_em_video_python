# Escreva um programa que converta uma temperatura digitada em °C para °F.

temperatura_celcius = float(input('Digite a temperatura em graus Celsiu: '))
temperatura_fahrenheit = ((temperatura_celcius * 9) / 5) + 32
vermelho = '\033[1;31m'
sem_cor = '\033[m'

print(f'Ao converter {vermelho}{temperatura_celcius}°C {sem_cor} para Fahrenheit, '
      f'temos: {vermelho}{temperatura_fahrenheit}°F {sem_cor}.')

