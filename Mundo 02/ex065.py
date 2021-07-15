# Aula 14

# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual
# foi o maior e o menor. O programa deve perguntar ao usuário se ele
# quer ou não continuar a digitar valores.

n = 0
condicao = ''
contador = soma = 0
maior = 0
menor = 0

while (condicao != 'N'):
  n = int(input('Digite um Número: '))
  condicao = input('Quer continuar [S/N]: ').upper()

  #------------
  soma += n
  contador += 1
  #------------
  if (contador == 1):
    maior = n
    menor = n
  elif (n > maior):
    maior = n
  elif (n < menor):
    menor = n

media = soma / contador
print(f'''Média: {media:.1f}
{maior} foi o maior número enquanto {menor} foi o menor.''')
