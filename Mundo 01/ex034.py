# Escreva um programa que pergunte o salário de um fincionário e
# calcule o valor do seu aumento. Para salários superiores a R$1.250,00,
# calcule um aumento de 10%. Para os inferior ou iguais, o aumento é de 15%

salario = float(input('Digite o valor do seu salário: R$ '))

if salario <= 1250:
  novo_salario = salario + (salario * 0.15)
  print(f'O seu salário, após o aumento de 15%, será igual a: R$ {novo_salario:.2f}.')
else:
  novo_salario = salario + (salario * 0.10)
  print(f'O seu salário, após o aumento de 10%, será igual a: R$ {novo_salario:.2f}.')

