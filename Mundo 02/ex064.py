# Aula 14

# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que
# é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre eles. Desconsiderando o flag.

print('''Enquanto você não disser "999", 
irei te pedir por novos número!''')

numero = contador = soma = 0

while (numero != 999):
    numero = int(input('Número: '))

    contador += 1
    soma += numero

print(f'''[Fim do Programa]
Você digitou {contador - 1} números
A soma de todos eles é: {soma - 999}''')