#Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz_q = n ** (1/2)

print(f'\033[7m O dobro de {n} é {dobro}, o triplo é {triplo} e a raiz quadrada é {raiz_q:.2f}. \033[m')

# maneira alternativa
# n = int(input('Digite um número: '))
# print(f'O dobro de {n} é {n * 2}, o triplo é {n * 3} e a raiz quadrada é {n ** (1/2)}.')
