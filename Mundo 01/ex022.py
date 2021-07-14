# Crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome_completo = str(input('Digite o seu nome completo: ')).strip()
print(f'Seu nome em maíusculo é: {nome_completo.upper()}.')
print(f'Seu nome em minúsculo é: {nome_completo.lower()}.')
print(f'O seu nome, ao todo, contém {len(nome_completo) - nome_completo.count(" ")} letras!')
print(f'O seu primeiro nome contém {len(nome_completo.split()[0])} letras!')

