# Aula 21

# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de motrar a ficha
# do jogador, mesmo que algum dado não tenha sico informado corretamente.

def ficha(jogador='<desconhecido>', gols=0):
    return print(f'O jogador {jogador} fez {gols} gol(s)!')


nome = input('Nome do jogador: ')
quantidade = input('Quantidade de gols: ')

if (quantidade.isnumeric() == False):
    quantidade = 0

if (nome == ''):
    ficha(gols=quantidade)
else:
    ficha(nome, quantidade)