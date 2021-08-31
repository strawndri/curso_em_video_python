from Aula_23.Ex115.registro.interface import *

def encontrado(analise):
    try:
        a = open(analise, 'rt')
        a.close()
    except FileNotFoundError:
        return False


def criarArquivo(arquivo):
    try:
        a = open(arquivo, 'wt+')
        a.close()
    except:
        formatar('[ERRO] -- Arquivo não foi criado.', 'vermelho')
