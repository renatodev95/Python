# Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para
# o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o
# usuário venceu ou perdeu.
from random import randint
from time import sleep
aleatorio = randint(0, 5)  # faz o computador escolher um numero entre 0 e 5
print('-=-' * 20)
print('Pensei em um número entre 0 e 5. Adivinha qual é... ')
print('-=-' * 20)
n = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
if n == aleatorio:
    print('Você acertou! Eu realmente pensei no número {}'.format(aleatorio))
else:
    print('Você errou! Eu tinha pensado no número {}'.format(aleatorio))
