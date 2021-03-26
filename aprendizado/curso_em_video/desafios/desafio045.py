from random import randint
from time import sleep
print('='*20, ' JO KEN PO ', '='*20)
print("""FAÇA SUA JOGADA:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jogador = int(input('Sua opção: '))
if jogador == 0 or jogador == 1 or jogador == 2:
    itens = ('PEDRA', 'PAPEL', 'TESOURA')
    computador = randint(0, 2)
    sleep(0.7)
    print('JO')
    sleep(0.7)
    print('KEN')
    sleep(0.7)
    print('PO!!!')
    print('='*20)
    print('O jogador escolheu {}!'.format(itens[jogador]))
    print('O computador escolheu {}!'.format(itens[computador]))
    if jogador == 0:  # jogador escolhe PEDRA
        if computador == 0:
            print('EMPATE!')
        elif computador == 1:
            print('O COMPUTADOR VENCEU!')
        elif computador == 2:
            print('O JOGADOR VENCEU!')
    if jogador == 1:  # jogador escolhe PAPEL
        if computador == 0:
            print('O JOGADOR VENCEU!')
        elif computador == 1:
            print('EMPATE!')
        elif computador == 2:
            print('O COMPUTADOR VENCEU!')
    if jogador == 2:  # jogador escolhe TESOURA
        if computador == 0:
            print('O COMPUTADOR VENCEU!')
        elif computador == 1:
            print('O JOGADOR VENCEU!')
        elif computador == 2:
            print('EMPATE!')
else:
    print('JOGADA INVÁLIDA')
