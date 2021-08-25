def moeda(valor):
    moeda = f'R$ {valor:.2f}'
    return moeda


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
    print('~-' * 15)
    print(f'{"Preço analisado:":<20}{moeda(preco)}')
    print(f'{f"{aumento}% de aumento:":<20}{aumentar(preco, aumento)}')
    print(f'{f"{reducao}% de reducao:":<20}{diminuir(preco, reducao)}')
    print(f'{"Metade do preço:":<20}{metade(preco)}')
    print(f'{"Dobro do preço:":<20}{dobro(preco)}')
    print('~-' * 15)
