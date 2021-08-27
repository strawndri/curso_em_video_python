# Aula 22

# Dentro do pacote utilidadesCev que criamos no desafio 111, temos um módulo chamado
# dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input()
# mas com uma validação de dados para aceitar apenas valores que sejam monetários.

from utilidadesCeV import moeda as md
from utilidadesCeV import dado

valor = dado.leiaDinheiro('Preço do produto, em reais: R$ ')
md.resumo(valor, 10, 20)
