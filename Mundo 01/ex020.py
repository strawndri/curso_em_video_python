# O mesmo professor do desafio anterior quer sortear a ordem de
# apresentação de trabalhos dos alunos. Faça um programa que leia
# o nome dos quatro alunos e mostre a ordem sorteada.

import random

nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ')
alunos = [nome1, nome2, nome3, nome4]
random.shuffle(alunos)

print(f'A ordem escolhida foi: {alunos}.')