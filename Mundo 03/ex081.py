# Aula 17

# Crie um programa que leia vários números e coloque-os em uma lista. Depois disso, mostre:
# a) Quantos números foram digitados;
# b) A lista de valores, ordenados de forma decrescente;
# c) Se o valor 5 foi digitado e está ou não na lista.

numeros = []
opcao = ''

while True:
  n = int(input('Digite um número: '))
  opcao = input('Deseja continuar? [S/N]').upper()

  numeros.append(n)

  if (opcao == 'N'):
    break

decrescente = numeros.copy()
decrescente.sort(reverse=True)

print('*-' * 15)
print(f'''Resultado Final: {numeros}
- Você digitou {len(numeros)} números
- Lista em ordem decrescente: {decrescente}''')
print(f'O valor 5 foi digitado {numeros.count(5)} vezes!' if (5 in numeros) else f'O valor 5 não foi digitado.')