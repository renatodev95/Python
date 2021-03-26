print('='*10+' LOJAS AMERICANAS '+'='*10)
compras = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opção = int(input('Qual é a opção? '))
if opção == 1:
    print('Sua compra de R${} vai custar R${} no final.'.format(compras, compras - (compras * 0.1)))
elif opção == 2:
    print('Sua compra de R${} vai custar R${} no final.'.format(compras, compras - (compras * 0.05)))
elif opção == 3:
    print('Sua compra de R${} vai sair pelo preço normal.'.format(compras))
elif opção == 4:
    qparcelas = int(input('Quantas parcelas? '))
    comprajuros = compras + (compras * 0.20)
    print('Sua compra será parcelada em {}x de R${} COM JUROS.'.format(qparcelas, comprajuros/qparcelas))
    print('Sua compra de R${} vai custar R${} no final.'.format(compras, comprajuros))
else:
    compras = 0
    print('[ERRO] SELECIONE UMA OPÇÃO DE PAGAMENTO VÁLIDA')
