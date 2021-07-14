# Faça um programa que leio o comprimento do cateto oposto e do cateto
# adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot

cateto_oposto = float(input('Digite o cateto oposto do seu triângulo retângulo: '))
cateto_adjacente = float(input('Digite o cateto adjacente do seu triângulo retângulo: '))
roxo = '\033[1;35m'
sem_cor = '\033[m'

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f'A hipotenusa do seu triângulo retângulo é: {roxo}{hipotenusa}{sem_cor}')