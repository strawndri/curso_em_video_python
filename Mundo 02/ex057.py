# Aula 14

# Faça um programa que leia o sexo de uma pessoa, mas só aceite os
# valores "M" ou "F". Caso esteja errado, peça a digitação novamente
# até o valor estar correto.

print('*-' * 10)
valor = input('Qual seu sexo? [M/F] ').upper()

while (valor != 'M' and valor !='F'):
  valor = input('''Tente novamente.
  Qual seu sexo? [M/F] ''').upper()
print('*-' * 10)