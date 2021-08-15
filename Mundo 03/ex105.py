# Aula 21

# Faça um programa que tenha a função notas() que pode receber várias notas de alunos e vai
# retornar um dicionário com as seguintes informações:

# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)

# Obs: Adicione a docstrings da função


def notas(*n, situacao=False):
  """\033[1;34m
  Função que analisa notas de vários alunos
  :param n: quantidade variável de notas
  :param situacao: [opcional] fornece ou não a situação, levando em consideração a média de notas
  :return: retorna um dicionário com: total de notas, maior e menor nota, média e situação
  \033[m
  """

  soma = 0
  for item in n:
    soma += item

  media = soma / len(n)

  r = {'Total': len(n),
       'Maior nota': max(n),
       'Menor nota': min(n),
       'Média': media}

  if (situacao == True):
    if (media >= 7 ):
      r['Situação'] = 'BOM'
    elif (media <= 5):
      r['Situação'] = 'RUIM'
    else:
      r['Situacao'] = 'REGULAR'

  return print(r)


notas(2, 5, 8, 10, 10, situacao=True)
help(notas)



