# Aula 16

# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:

# Apenas os 5 primeiros colocados.
# Os últimos 4 colocados da tabela.
# Uma lista com os times em ordem alfabética
# Em que posição na tabela está o time da Chapecoense.

times = ('Palmeiras', 'Atlético-MG', 'Fortaleza', 'Bragantino', 'Athletico-PR',
        'Flamengo', 'Ceará', 'Bahia', 'Fluminense', 'Santos', 'Atlético-GO',
        'Corinthians', 'Internacional', 'Juventude', 'São Paulo', 'América-MG',
        'Cuiabá',	'Sport', 'Grêmio', 'Chapecoense')

print(f'Times do Campeonato Brasileiro de Futebol: {times}')
print(f'Os cinco primeiros colocados: {times[:5]}')
print(f'Os últimos quatro colocados da tabela: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)} ')
print(f'A Chapecoense está na posição {times.index("Chapecoense") + 1}')