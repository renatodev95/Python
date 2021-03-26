def aumentar(preco, taxa=0):
    res = preco + (preco*(taxa/100))
    return res


def diminuir(preco, taxa=0):
    res = preco - (preco * taxa/100)
    return res


def dobro(preco):
    return preco*2


def metade(preco):
    return preco/2
