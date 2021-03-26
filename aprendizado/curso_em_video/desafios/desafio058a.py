from random import randint
computador = randint(0, 1)  # faz o computador escolher um numero entre 0 e 5
print('Sou seu computador... \nAcabei de pensar em um número entre 0 e 10. \nSerá que você consegue advinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente.')
        elif jogador > computador:
            print('Menos... Tente novamente.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
