cores = {'normal': '\033[01;m',
         'vermelho': '\033[01;31m',
         'amarelo': '\033[01;33m',
         'roxo': '\033[01;35m'}


def formatar(texto, cor=cores['normal'], linha=False):
    if (linha == True):

        print(f'{cores["normal"]}-' * 50)
        print(f'{cores[cor]}{texto}{cores["normal"]}'.center(60))
        print(f'{cores["normal"]}-' * 50)
    else:
        print(f'{cores[cor]} {texto} {cores["normal"]}')

#-------------------------------------------------------------------------------
import json
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
            lista()
        elif (escolha == 2):
            cadastrar()
        else:
            formatar('> Fim da Execução. Obrigada por utilizar o sistema.', 'roxo')


def salvar(usuario):
    arquivo = open('./cadastrados.txt', 'w')
    arquivo.write(json.dumps(usuario))
    arquivo.close()




