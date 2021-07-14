# Aula 14

# Melhore o jogo do desafio 028, em que o computador vai pensar em um
# número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até
# acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randrange
from time import sleep

cores = {
    0 : '\033[m',
    1 : '\033[1;031m',
    2 : '\033[1;32m',
}
n_aleatorio = randrange(1,10)
contador = 0

print('[ Será que você consegue acertar o número que eu pensei? ]')
n_resposta = int(input('Tente descobrir o número escolhido pelo computador. Digite um valor entre 0 e 10: '))
print('~' * 82)
print('Carregando...')
sleep(1)

while (n_resposta != n_aleatorio):
  n_resposta = int(input(f'{cores[1]}Você errou! Tente novamente: {cores[0]}'))
  contador += 1

print(f'''{cores[2]}Parabéns, você acertou! O número era {n_aleatorio}.
{cores[0]}Número de tentativas {contador +1 }.''')