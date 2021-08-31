# Aula_23

# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um
# arquivo de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoas e listar todas
# as pessoas cadastradas.

from registro import arquivo as a
from registro import cadastro as c
from registro import interface as i
from time import sleep
import json

arquivo = 'cadastrados.txt'

while True:
    if (a.encontrado(arquivo) == False):

        i.formatar('[ERRO] -- O Programa não pode ser iniciado', 'vermelho', linha=True)
        opcao = input('Deseja criar um arquivo para continuar? [S/N] ').upper().split()[0]

        if (opcao == 'S'):
            i.formatar('Aguarde um momento...', 'roxo', linha=True)
            sleep(2)
            a.criarArquivo(arquivo)
            arquivo = open('./cadastrados.txt', 'r')
            arquivo = arquivo.read()
        else:
            i.formatar('Obrigada por utilizar nosso sistema.', 'roxo', linha=True)
            sleep(1)
            break

    try:
        pessoas = json.loads(arquivo)
    except:
        pessoas = []

    c.sistema(pessoas)
    break













