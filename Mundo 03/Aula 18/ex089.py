# Aula 18

# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
# notas de cada aluno individualmente.

turma = []
aluno = []
notas = []
media = 0

while True:
    aluno.append(input('Nome: '))
    notas.append(float(input('1° Nota: ')))
    notas.append(float(input('2° Nota: ')))

    opcao = ' '
    while (opcao not in 'SN'):
        opcao = input('Deseja continuar? [S/N] ').upper()

    aluno.append(notas[:])
    turma.append(aluno[:])

    notas.clear()
    aluno.clear()

    if (opcao == 'N'):
        break

print('^^' * 15)
print(f'{"BOLETIM ESCOLAR":^30}')
print('^^' * 15)
print(f'{"N°":<3} Nome {"Média":>20}')
print('-' * 30)

for key, aluno in enumerate(turma):
    media = (aluno[1][0] + aluno[1][1]) / 2

    print(f'{key:<3} {aluno[0]:<20} {media:.2f}')

while True:
    print('-' * 30)
    n = int(input('Mostrar notas de qual aluno? (999 para parar) '))

    if (n == 999):
        break

    print(f'Notas de {turma[n][0]}: {turma[n][1]}')
