from random import randint
print('=-='*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-='*15)
vit = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print('--' * 15)
    if escolha == 'P':
        if (jogador+computador) % 2 == 0:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador+computador} DEU PAR!')
            print('--' * 15)
        else:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador+computador} DEU ÍMPAR!')
            print('--' * 15)
    if escolha == 'I':
        if (jogador + computador) % 2 == 0:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador} DEU PAR!')
            print('--' * 15)
        else:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador} DEU ÍMPAR!')
            print('--' * 15)
    if escolha == 'P' and (jogador+computador) % 2 == 0:
        vit += 1
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-=' * 15)
    if escolha == 'I' and (jogador+computador) % 2 != 0:
        vit += 1
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-=' * 15)
    if escolha == 'P' and (jogador+computador) % 2 != 0:
        print('Você PERDEU!')
        print('=-=' * 15)
        break
    if escolha == 'I' and (jogador+computador) % 2 == 0:
        print('Você PERDEU!')
        print('=-=' * 15)
        break
print(f'GAME OVER! Você venceu {vit} vezes.')
