from random import randint
computador = randint(0, 1)  # faz o computador escolher um numero entre 0 e 5
print('-=-' * 20)
print('Sou seu computador... \nAcabei de pensar em um número entre 0 e 10. \nSerá que você consegue advinhar qual foi?')
print('-=-' * 20)
jogador = int(input('Qual é seu palpite? '))
tentativas = 1
while jogador != computador:
    tentativas += 1
    if jogador > computador:
        print('Menos... Tente mais uma vez.')
        jogador = int(input('Qual é seu palpite? '))
    elif jogador < computador:
        print('Mais... Tente mais uma vez')
        jogador = int(input('Qual é seu palpite? '))
print('Acertou com {} tentativas. Parabéns!'.format(tentativas))
