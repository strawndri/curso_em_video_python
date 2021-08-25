# Aula 19

# Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando
# os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:

# Quantas pessoas foram cadastradas;
# A média de idade do grupo;
# Uma lista com todas as mulheres;
# Uma lista com todas as pessoas com idade acima da média.


from datetime import date

ano_atual = date.today().year

grupo = []
pessoa = {}
mulheres = []
acima_media = []
pessoas = 0
total_idades = 0
media = 0

while True:

    pessoa['Nome'] = input('Nome: ')

    sexo = ' '
    while (sexo not in 'FM'):
        sexo = input('Sexo:').upper()
    pessoa['Sexo'] = sexo

    nascimento = int(input('Ano de nascimento: '))
    pessoa['Idade'] = (ano_atual - nascimento)

    grupo.append(pessoa.copy())
    pessoa.clear()

    opcao = ' '
    while (opcao not in 'SN'):
        opcao = input('Deseja continuar? [S/N] ').upper()

    if (opcao == 'N'):
        break

print('^^^' * 15)

for item in grupo:

    pessoas += 1

    for key, value in item.items():

        if (key == 'Idade'):
            total_idades += value
        elif (key == 'Sexo' and value == 'F'):
            mulheres.append(item['Nome'])

        if (pessoas == len(grupo)):
            media = (total_idades / pessoas)

for item in grupo:
    for key, value in item.items():
        if (key == 'Idade' and value > media):
            acima_media.append(item['Nome'])

print(f'Há {pessoas} pessoas no grupo.')
print(f'A média das idades é de {media:.1f} anos.')

print(f'A mulheres do grupo são: ', end='')
for item in mulheres:
    print(item, end='; ')
print()

print(f'A pessoa com a idade acima de {media:.1f} são: ', end='')
for item in acima_media:
    print(item, end='; ')
print()

