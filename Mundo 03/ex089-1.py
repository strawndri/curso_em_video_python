# Aula 18

# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
# notas de cada aluno individualmente.

turma = []

while True:
    nome = (input('Nome: '))
    n1 = (float(input('1° Nota: ')))
    n2 = (float(input('2° Nota: ')))
    media = (n1 + n2) / 2

    opcao = ' '
    while (opcao not in 'SN'):
        opcao = input('Deseja continuar? [S/N] ').upper()

    turma.append([nome, [n1, n2], media])

    if (opcao == 'N'):
        break

print('^^' * 16)
print(f'{"BOLETIM ESCOLAR":^30}')
print('^^' * 16)
print(f'{"N°":<3} {"Nome":<10} {"Média"} {"Resultado":>10}')
print('-' * 32)

for key, aluno in enumerate(turma):

    if (aluno[2] >= 7.0):
        resultado = 'Aprovado'
    elif (aluno[2] <= 5.0):
        resultado = 'Reprovado'
    else:
        resultado = 'Recuperação'

    print(f'{key:<3} {aluno[0]:<10} {aluno[2]:.2f} {resultado:>12}')

while True:
    print('-' * 32)
    n = int(input('Mostrar notas de qual aluno? (999 para parar) '))

    if (n == 999):
        break

    print(f'Notas de {turma[n][0]}: {turma[n][1]}')
