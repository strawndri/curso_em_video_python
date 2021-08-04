# Aula 19

# Aprimore o desafio 093 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador.

time = []
jogador = {}

print(f'{"CAMPEONATO DE FUTEBOL":^36}')

while True:
    print('=~' * 18)
    jogador['Nome'] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    gols = list()
    total_gols = 0

    for item in range(0, partidas):
        quantidade_gols = int(input(f'   Gols na {item + 1}° partida: '))
        gols.append(quantidade_gols)

        total_gols += quantidade_gols

    jogador['Gols'] = gols
    jogador['Total'] = total_gols

    time.append(jogador.copy())
    jogador.clear()

    opcao = ' '
    while (opcao not in ('SN')):
        opcao = input('Deseja continuar? [S/N] ').upper()

    if (opcao == 'N'):
        break

print('=~' * 18)
print(f'{"n°":<2} {"Nome":<10} {"Gols":<15} {"Total":>}')

for i, item in enumerate(time):
    print(f'{i:<2} {item["Nome"]:<10} {str(item["Gols"]):<15} {item["Total"]}')

while True:
    print('=~' * 18)
    numero = int(input('Qual jogador deseja ver os dados? (999 para parar) '))

    if (numero == 999):
        break
    elif (numero > len(time) - 1 and numero != 999):
        numero = int(input('[ERRO] --- digite um número válido: '))
    else:
        print(f'   Levantamento de {time[numero]["Nome"].upper()}')

        for i, item in enumerate(time[numero]['Gols']):
            print(f'   {i + 1}º Jogo: {item} gols')