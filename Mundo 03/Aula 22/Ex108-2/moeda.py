def moeda(valor, moeda='R$'):
    novo_valor = f'{moeda} {valor:.2f}'
    return novo_valor


def aumentar(preco):
    novo_preco = preco + (preco * 0.10)

    return novo_preco


def diminuir(preco):
    novo_preco = preco - (preco * 0.10)

    return novo_preco


def dobro(preco):
    novo_preco = preco * 2

    return novo_preco


def metade(preco):
    novo_preco = preco /2

    return novo_preco


