def moeda(valor, moeda='R$'):

    novo_valor = f'{moeda} {valor:.2f}'
    return novo_valor.replace('.', ',')


def aumentar(preco, porcentagem, formatacao=True):
    novo_preco = preco + (preco * (porcentagem/100))

    if (formatacao):
        novo_preco = moeda(novo_preco)

    return novo_preco


def diminuir(preco , porcentagem, formatacao=True):
    novo_preco = preco - (preco * (porcentagem/100))

    if (formatacao):
        novo_preco = moeda(novo_preco)

    return novo_preco


def dobro(preco, formatacao=True):
    novo_preco = preco * 2

    if (formatacao):
        novo_preco = moeda(novo_preco)

    return novo_preco


def metade(preco, formatacao=True):
    novo_preco = preco /2

    if (formatacao):
        novo_preco = moeda(novo_preco)

    return novo_preco


def resumo(preco, aumento, reducao):

    print('- ' * 15)
    print(f'Resumo do Preço'.center(30))
    print('- ' * 15)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento)}')
    print(f'{reducao}% de redução: \t{diminuir(preco, reducao)}')
    print(f'Metade do Preço: \t{metade(preco)}')
    print(f'Dobro do Preço: \t{dobro(preco)}')
    print('- ' * 15)
