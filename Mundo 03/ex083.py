# Aula 17

# Crie um programa que o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
# e fechados na ordem correta.

expressao = input('Digite a expressão matemática: ').split()
open = close = 0

for item in range(0, len(expressao)):
  if '(' in expressao[item]:
    open += 1
  elif ')' in expressao[item]:
    close += 1

print('Sua expressão está correta!' if open == close else 'Sua expressão está incorreta!')