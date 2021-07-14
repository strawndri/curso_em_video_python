# Aula 13

# Refaça o desafio 009, mostrando a tabuada de um número que
# o usuário escolher, só que agora utilizando um laço for.

print('-*' * 20)
numero = int(input('Digite um número: '))

for item in range(0, 11):
  resultado = item * numero
  print(f'{numero} x {item} = {resultado}')
print('-*' * 20)