#Desenvolva um programa que leia duas notas de um aluno, calcule e mostre sua média.

n1 = float(input('Digite a nota número 01: '))
n2 = float(input('Digite a nota número 02: '))
media = (n1 + n2) / 2

print(f'A média das notas {n1} e {n2} equivale a: {media:.1f}.')
