# Aula 19

# Faça um programa que leia o nome e a média de um aluno, guardando também a
# situação em um dicionário. No final, mostre o conteúdo da estrutura na tela

aluno = {}
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input('Média final: '))

if (aluno['media'] <= 5):
    aluno['situacao'] = 'Reprovado'
elif (aluno['media'] >= 7):
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Recuperação'

print('*-' * 15)
print(f'''Nome: {aluno["nome"]}
Média Final: {aluno["media"]}
Situação: {aluno["situacao"]}''')