# Aula_23

# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um
# arquivo de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoas e listar todas
# as pessoas cadastradas.

from registro import arquivo as a
from registro import cadastro as c
import json

arquivo = 'cadastrados.txt'

if (a.encontrado(arquivo) == False):
    a.criarArquivo(arquivo)

arquivo = open('./cadastrados.txt', 'r')
arquivo = arquivo.read()

try:
    pessoas = json.loads(arquivo)
except:
    pessoas = []

c.sistema(pessoas)








