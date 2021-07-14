# Aula

# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem final, de acordo com a média antigida:

# Abaixo de 5.0: Reprovado
# Entre 5.0 e 6.9: Recuperação
# 7.0 ou Superior: Aprovado

nota1 = float(input('Nota 01: '))
nota2 = float(input('Nota 02: '))

media = (nota1 + nota2) / 2
print(f'Sua média foi: {media}')

if (media < 5.0):
  print('Reprovado!')
elif (media >= 5.0) and (media <= 6.9):
  print('Recuperação!')
else:
  print('Aprovado!')