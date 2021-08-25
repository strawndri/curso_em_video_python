# Aula 20


# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável.


def escreva(texto):

    largura = len(texto) + 2

    print('=' * largura)
    print(f' {texto} ')
    print('=' * largura)

escreva('Andrieli Luci Gonçalves')
escreva('Texto')


