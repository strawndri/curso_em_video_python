# Aula 18

# Aprimore o desafio anterior, mostrando no final:

# A soma de todos os valores pares digitados;
# A soma dos valores da terceira coluna;
# O maior valor da segunda linha;

matriz = [[],
          [],
          []]
soma_pares = 0
soma_column = 0
maior = 0

for row in range(0, 3):
    for column in range(0, 3):
        valor = int(input((f'Digite um valor para {(row, column)}: ')))
        matriz[row].append(valor)

print('*-' * 15)

for key, row in enumerate(matriz):

    for item in row:
        print(f'[{item}]', end='')

        if (item % 2 == 0):
            soma_pares += item

        if (key == 1):
            maior = max(row)

        if (item == row[2]):
            print(end='\n')

    soma_column += row[2]

print('*-' * 15)
print(f'''Soma de todos os valores pares: {soma_pares} 
Soma da terceira coluna: {soma_column}
Maior valor da segunda linha: {maior}''')