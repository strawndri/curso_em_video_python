# Aula 13

# Faça um programa que calcule a soma entre todos os números
# ímpares que são múltiplos de três e que se encontram no intervalo
# de 1 até 500.


soma = 0
for item in range(0, 501, 3):
  if (item % 2 == 1):
    soma += item
print(f'Resultado: {soma}')