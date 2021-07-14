# Faça um programa que leia uma frase pelo teclado e mostre:

# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().upper()

print(f'A letra "A" aparece {frase.count("A")} vezes em sua frase.')
print(f'Ela aparece, pela primeira vez, na posição {frase.find("A") + 1}.')
print(f'Ela aparece, pela última vez, na posição {frase.rfind("A") + 1}.')

