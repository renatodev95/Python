# Faça um programa que tenha uma função chamada área(), que receba as dimensões
# de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def titulo(txt):
    print('-' * 30)
    print(f'{txt:^30}')
    print('-' * 30, '')


def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².\n')


titulo('CONTROLE DE TERRENO')
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
