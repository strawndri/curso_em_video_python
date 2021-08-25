# Aula 22

# Adapte o código do desafio 107, criando uma função adicional chamada moeda()
# que consiga mostrar os valores como um valor monetário formatado.

# ---------------------------------------------------------------------------

import moeda as md

valor = float(input('Digite um valor, em reais: R$ '))

print(f'Aumentando {md.moeda(valor)} em 10%, tem-se: {md.moeda(md.aumentar(valor))}')
print(f'Diminuindo {md.moeda(valor)} em 10%, tem-se: {md.moeda(md.diminuir(valor))}')
print(f'O dobro de {md.moeda(valor)} é: {md.moeda(md.dobro(valor))}')
print(f'A metade de {md.moeda(valor)} é: {md.moeda(md.metade(valor))}')