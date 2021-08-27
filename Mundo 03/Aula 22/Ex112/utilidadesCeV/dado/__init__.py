def leiaDinheiro(texto):
    valor = input(texto).strip()

    while True:

        if (',' in valor):
            valor = valor.replace(',', '.')

        if(valor.isnumeric() or valor.replace('.', '').isnumeric()):
            break

        print(f'''\033[01;31m[ERRO] - "{valor}" não é um valor monetário - [ERRO]\033[m''')
        valor = input('Digite novamente: ')

    return float(valor)

