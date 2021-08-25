def moeda(valor, moeda='R$'):
    novo_valor = f'{moeda} {valor:.2f}'
    return novo_valor


def aumentar(preco, formatacao=True):
    novo_preco = preco + (preco * 0.10)

    if (formatacao):
        novo_preco = moeda(novo_preco)

    return novo_preco


def diminuir(preco, formatacao=True):
    novo_preco = preco - (preco * 0.10)

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


