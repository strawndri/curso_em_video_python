# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome_completo = str(input('Digite o seu nome completo: ')).strip()
print(f'Seu primeiro nome é: {nome_completo.split()[0]}.')
print(f'Seu último nome é : {nome_completo.split()[-1]}.')

