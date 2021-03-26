# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
real = float(input('Quanto dinheiro você tem na carteira? '))
dolar = real / 3.27
print('Você pode comprar ${:.2f} dólares com R${:.2f} reais.'.format(dolar, real))
