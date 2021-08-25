# Aula 22

# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e
# mantenha tudo funcionando.

from utilidadesCeV import moeda as md

valor = float(input('Preço do produto, em reais: R$ '))
md.resumo(valor, 10, 20)
