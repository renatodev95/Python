# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário
# vai continuar. No final, mostre: a)Qual é o TOTAL GASTO na compra; b)Quantos produtos custam mais de R$1000;
# c)Qual é o NOME do produto mais barato.
print('-'*60)
loja = 'LOJA SUPER BARATÃO'
print(f'{loja:^60}')
print('-'*60)
nomebarato = ''
barato = 0
cont = 0
totgasto = 0
totmaismil = 0
while True:
    nomeproduto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    continuar = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    totgasto += preço
    if preço > 1000:
        totmaismil += 1
    if cont == 0:
        barato = preço
        nomebarato = nomeproduto
    else:
        if preço < barato:
            nomebarato = nomeproduto
            barato = preço
    cont += 1
    if continuar == 'N':
        break
print('-'*20, ' FIM DO PROGRAMA ', '-'*20)
print(f'O total da compra foi R${totgasto:.2f}')
print(f'Temos {totmaismil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomebarato} que custa R${barato:.2f}')
