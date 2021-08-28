# Aula 23

# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade
# da digitação de um número de tipo inválido. Aproveite e crie também uma função
# leiaFloat() com a mesma funcionalidade.

def leiaInt(texto):
    while True:

        try:
            numero = int(input(texto))
        except:
            print(f'\033[01;31m -- [ERRO: número digitado é inválido] -- \033[m')
        else:
            break

    return numero


def leiaFloat(texto):
    while True:

        try:
            numero = float(input(texto))
        except:
            print(f'\033[01;31m -- [ERRO: número digitado é inválido] -- \033[m')
        else:
            break

    return numero


n1 = leiaInt('Número Inteiro: ')
n2 = leiaFloat('Número Real: ')

print(f'Números digitados: {n1} e {n2}')
