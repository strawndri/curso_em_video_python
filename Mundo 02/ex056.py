# Aula 13

# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos

soma_idades = 0
maior = 0
nome_mais_velho = ''
contador = 0

for item in range(1, 5):
  nome = input('Nome: ')
  idade = int(input('Idade: '))
  sexo = input('Sexo (M ou F): ')
  print('-' * 12)

  soma_idades += idade
  media = soma_idades / 4

  if (sexo == 'M'):
    if (idade > maior):
      maior = idade
      nome_mais_velho = nome

  if (sexo == 'F' and idade < 20):
    contador += 1

print(f'Média das idades: {media}')
print(f'Com {maior} anos, {nome_mais_velho} é o homem mais velho.')
print(f'Há {contador} mulheres com menos de 20 anos.')