# Aula 16

# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('desenhar', 'livro', 'programação', 'morango', 'tartaruga', 'alecrim')
print('Quais vogais há em cada palavra? ')
print('=-' * 15)

for item in palavras:
    print(item, end=': ')
    l = 0

    while True:
        if (item.split()[0][l] in 'aeiou'):
            print(item.split()[0][l], end=' ')

        l += 1

        if (l == len(item)):
            print('\n')
            break
