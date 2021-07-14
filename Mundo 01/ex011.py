# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo
# que cada litro de tinta pinta uma área de 2m².

verde = '\033[1;36m'
sem_cor = '\033[m'

largura = float(input('Insira a largura da parede: '))
altura = float(input('Insira a altura da parede: '))
area = largura * altura
tinta_necessaria = area / 2

print(f'Sua parede possui {verde}{area}m²{sem_cor} de área.')
print(f'Você precisará de {verde}{tinta_necessaria}{sem_cor} litros de tinta para pintá-la.')

