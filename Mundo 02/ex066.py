# Aula 15

# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai
# parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
# mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

n = soma = contador = 0

while (True):
  n = int(input('Digite um número (999 para parar): '))

  if (n == 999):
    break
  soma += n
  contador += 1
print(f'''[Fim da Execução]
A soma dos {contador} números é : {soma}''')