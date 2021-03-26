# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Informe o preço do produto: R$'))
novo = preco - (preco * 0.05)
print('O produto que custava R${:.2f}, na promoção, com 5% de desconto vai custar: R${:.2f} reais.'.format(preco, novo))
