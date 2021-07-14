# Aula 13

# Crie um programa que leia uma frase qualquer e diga se ela é um políndromo, desconsiderando os espaços.

texto = input('Digite uma palavra ou frase: ').strip().lower()
texto2 = texto.replace(" ", "")
novo_texto = ''

for item in range(len(texto2), 0, -1):
  novo_texto += texto2[item-1]

if (novo_texto == texto2):
  print(f'{texto.upper()} é um políndromo, ou seja, é igual de trás para frente!')
else:
   print(f'{texto.upper()} não é um políndromo, ou seja, não é igual de trás para frente!')