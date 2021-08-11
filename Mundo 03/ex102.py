# Aula 21

def fatorial(n, show=False):
  """\033[31;1m
  > Calcular o Fatorial de Determinado Número
    :param n: valor que será calculado
    :param show: (opcional) mostrar ou não o cálculo
    :return: retorna o resultado do fatorial de um número
  """

  resultado = 1
  print(f'{n}!', end=' = ')

  for item in range(n, 0, -1):

    if (show == True):
      print(f'{item} = ' if (item == 1) else f'{item} x ', end='')
    resultado *= item

  return resultado

fatorial(6, False)
help(fatorial)