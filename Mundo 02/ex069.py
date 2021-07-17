# Aula 15

# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoas cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# Quantas pessoas tem mais de 18 anos
# Quantos homens foram cadastrados
# Quantas mulheres tem menos de 20 anos

print('==' * 15)
print('CADASTRO')
print('==' * 15)

maior_idade = homem = mulher_jovem = 0

while (True):

  idade = int(input('Idade: '))
  sexo = continuar = ' '

  while (sexo not in ('FfMm')):
    sexo = input('Sexo [F/M]: ')

  while (continuar not in ('SsNn')):
    continuar = input('Deseja Continuar? [S/N] ')

  if (idade > 18):
    maior_idade += 1
  if (sexo in 'Mm'):
    homem += 1
  if ((idade < 20) and (sexo in ('Ff'))):
    mulher_jovem += 1

  if (continuar in ('Nn')):
    print('==' * 15)
    print('FIM DA EXECUÇÃO')
    print('==' * 15)
    break

print(f'''
Pessoas maiores de 18 anos: {maior_idade}
Quantidade de homens cadastrados: {homem}
Mulheres menores de 20 anos: {mulher_jovem}''')