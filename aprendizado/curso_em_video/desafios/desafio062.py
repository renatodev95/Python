primeitoTermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
ntermos = 0
cont = 1
op = 10
while op != 0:
    ntermos += op
    while cont <= ntermos:
        print(f'{primeitoTermo} ➡', end=' ')
        primeitoTermo += razao
        cont += 1
    print('PAUSA')
    op = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {ntermos} termos mostrados.')
