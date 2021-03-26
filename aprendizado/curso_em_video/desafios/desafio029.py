"""Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite."""

velocidade = float(input('Qual foi a velocidade do carro em Km/h? '))
if velocidade > 80:
    print('\033[31mVocê ultrapassou o limite de velocidade e foi MULTADO\033[m. \033[33mO valor da multa é de R${:.2f}\033[m'.format((velocidade-80)*7))
else:
    print('Você não ultrapassou o limite. Continue assim!')
