def aumentar(preco=0, taxa=0, formata=False):
    res = preco + (preco * (taxa / 100))
    return res if formata is False else moeda(res)  # MÉTODO DE ESCOLHA DE RET.


def diminuir(preco=0, taxa=0, formata=False):
    res = preco - (preco * taxa/100)
    return res if not formata else moeda(res)  # MÉTODO DE ESCOLHA DE RETORNO


def dobro(preco=0, formata=False):
    res = preco * 2
    return res if not formata else moeda(res)  # MÉTODO DE ESCOLHA DE RETORNO


def metade(preco=0, formata=False):
    res = preco / 2
    return res if not formata else moeda(res)  # MÉTODO DE ESCOLHA DE RETORNO


def moeda(preco=0.0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
