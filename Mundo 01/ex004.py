#Faça um programa que leia algo pelo teclado e mostra na tela
# o seu tipo primitivo e todas as informações possíveis sobre ele.

resposta = input('Digite qualquer coisa: ')
print(f'{resposta} é do tipo ', type(resposta))
print('Só tem espaços? ', resposta.isspace())
print('Só tem números (numérico)? ', resposta.isnumeric())
print('Só tem letras (alfabético)? ', resposta.isalpha())
print('Está apenas em maiúsculo? ', resposta.isupper())
print('Está apenas em minúsculo? ', resposta.islower())
