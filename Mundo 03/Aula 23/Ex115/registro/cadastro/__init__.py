#-------------------------------------------------------------------------------
from Aula_23.Ex115.registro.interface import *

import json
from time import sleep

arquivo = open('./cadastrados.txt', 'r')
a = arquivo.read()

usuario = {}
pessoas = []

try:
    pessoas = json.loads(a)
except:
    pessoas = []

def lista():
    if (len(pessoas) == 0):
        opcao = input('''Não há pessoas na lista,
Deseja Cadastrar um novo usuário? [S/N] ''').upper().split()[0]

        if (opcao == 'S'):
            cadastrar()
    else:
        formatar('Pessoas Cadastradas', 'roxo', linha=True)

        for item in pessoas:
            print(f'{item["nome"]:<40} {item["idade"]} anos')


def cadastrar():
    usuario['nome'] = input('Nome: ')
    usuario['idade'] = (input('Idade: '))

    pessoas.append(usuario.copy())
    usuario.clear()

    salvar(pessoas)


def salvar(usuario):
    arquivo = open('./cadastrados.txt', 'w')
    arquivo.write(json.dumps(usuario))
    arquivo.close()


def sistema():

    while True:

        while True:

            formatar('MENU PRINCIPAL', 'roxo', linha=True)

            formatar('''[1]  Ver pessoas cadastradas
[2]  Cadastrar pessoa nova
[3]  Sair do sistema''', 'amarelo', linha=True)

            try:
                escolha = int(input('Escolha uma das opções acima: '))
            except (ValueError, TypeError):
                formatar('> [ERRO] -- Digite um número inteiro válido!', 'vermelho')
            except KeyboardInterrupt:
                formatar('> [ERRO] -- O usuário não continuou o processo.', 'vermelho')
            else:
                if (escolha == 1 or escolha == 2 or escolha == 3):
                    break
                else:
                    formatar('> [ERRO] -- Digite um número da lista!', 'vermelho')
                    continue

        if (escolha == 1):
            formatar('Carregando Lista de Cadastrados...', 'amarelo', linha=True)
            sleep(1)
            lista()
        elif (escolha == 2):
            formatar('Carregando Sistema de Cadastro...', 'amarelo', linha=True)
            sleep(1)
            cadastrar()
        else:
            formatar('> Fim da Execução. Obrigada por utilizar o sistema.', 'roxo', linha=True)
            sleep(1)
            break






