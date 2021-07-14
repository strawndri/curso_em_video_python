# Aula

# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40 Obesidade
# Acima de 40: Obesidade mórbida

altura = float(input('Altura: '))
peso = float(input('Peso: '))

imc = peso / (altura ** 2)

print(f'IMC: {imc:.2f}')

if (imc < 18.5):
  print('Você está abaixo do peso.')
elif (imc >= 18.5 and imc <= 25):
  print('Você com o Peso ideal.')
elif (imc > 25 and imc <= 30):
  print('Você está em Sobrepeso.')
elif (imc > 30 and imc <= 40):
  print('Você está em Obesidade.')
else:
  print('Você está em Obesidade mórbida.')
