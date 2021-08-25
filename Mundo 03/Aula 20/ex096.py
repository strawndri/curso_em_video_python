# Aula 20

# Faça um programa que tenha uma função chamada area(),
# que recebe as dimensões de um terreno retangular (largura e comprimento) e mostra a área do terreno.

def criaTitulo(titulo):
  print('*-' * 15)
  print(f'{titulo:^30}')
  print('*-' * 15)


def area(largura, comprimento):
  area = largura * comprimento
  print(f'A área do terreno de [{largura} x {comprimento}] é: {area}m². ')


criaTitulo('Tamanho do Terreno')

l = float(input('Largura (em metros): '))
c = float(input('Comprimento (em metros): '))

area(l, c)


