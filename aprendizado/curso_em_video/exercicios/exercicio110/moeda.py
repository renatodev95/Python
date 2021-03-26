def aumentar(preco=0, taxa=0, form=False):
    res = preco + (preco * (taxa / 100))
    # MÉTODO DE ESCOLHA DE RETORNO NA MESMA LINHA
    return res if form is False else moeda(res)


def diminuir(preco=0, taxa=0, form=False):
    res = preco - (preco * taxa/100)
    # MÉTODO DE ESCOLHA DE RETORNO NA MESMA LINHA
    return res if not form else moeda(res)


def dobro(preco=0, form=False):
    res = preco * 2
    # MÉTODO DE ESCOLHA DE RETORNO NA MESMA LINHA
    return res if not form else moeda(res)


def metade(preco=0, form=False):
    res = preco / 2
    # MÉTODO DE ESCOLHA DE RETORNO NA MESMA LINHA
    return res if not form else moeda(res)


def moeda(preco=0.0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=0, taxar=0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('-'*30)

#  O \t é utilizado como tabulação dentro da função PRINT