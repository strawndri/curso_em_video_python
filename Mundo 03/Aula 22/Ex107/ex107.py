# Aula 22

# Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade().

# Faça também um programa que importe esse módulo e use algumas dessas funções.

# ---------------------------------------------------------------------------

import moeda as md

valor = float(input('Digite um valor, em reais: R$ '))

print(f'Aumentando {valor} em 10%, tem-se: R$ {md.aumentar(valor):.2f}')
print(f'Diminuindo {valor} em 10%, tem-se: R$ {md.diminuir(valor):.2f}')
print(f'O dobro de {valor} é: R$ {md.dobro(valor):.2f}')
print(f'A metade de {valor} é: R$ {md.metade(valor):.2f}')