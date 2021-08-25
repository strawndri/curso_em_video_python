# Aula 22

# Modifique as funções que foram criados no desafio 107 para que elas aceitem
# um parâmetro a mais, informando se o valor retornado por ela vai ser ou não
# formatado pela função moeda(), desenvolvida no desafio 108

# ---------------------------------------------------------------------------

import moeda as md

valor = float(input('Digite um valor, em reais: R$ '))

print(f'Aumentando {md.moeda(valor)} em 10%, tem-se: {md.aumentar(valor, True)}')
print(f'Diminuindo {md.moeda(valor)} em 10%, tem-se: {md.diminuir(valor, True)}')
print(f'O dobro de {md.moeda(valor)} é: {md.dobro(valor, True)}')
print(f'A metade de {md.moeda(valor)} é: {md.metade(valor, False)}')