# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano % 4 == 0 or ano % 400 == 0 and not ano % 100 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO!'.format(ano))
