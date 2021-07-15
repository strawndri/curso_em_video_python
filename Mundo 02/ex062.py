# Aula 14

# Melhore o desafio 061, perguntando ao usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer 0 termos.

n1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
contador = 0
termo = 10

while (contador < (termo)):
  print(f'{n1}', end = ' -> ')
  n1 += razao
  contador += 1

  if (contador == (termo)):
    print('[Pausa]')
    novo_termo = int(input('Quantos termos a mais você deseja? '))
    termo += novo_termo
print(f'''Fim da Progressão Aritmética de {termo} termos!''')