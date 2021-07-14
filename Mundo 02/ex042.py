# Aula

# Refaça o desafio 035 dos triânuglos,
# acrescentando o recurso de mostrar que tipo de
# triângulo será formado (Equilátero, Isósceles ou Escaleno)

l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
  if (l1 == l2) and (l1 == l3):
    print('Seu triângulo é equilátero.')
  elif (l1 != l2) or (l1 != l3):
    print('Seu triângulo é escaleno.')
  else:
    print('Seu triângulo é isósceles.')
else:
  print('Você não pode formar um triângulo.')