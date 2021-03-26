cont = 1
while True:
    num = int(input('Quer ver a tabuada de qual valor: '))
    if num < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
    cont = 1
    print('-'*20)
    while cont <= 10:
        print(f'{num} x {cont:2} = {num*cont:2}')
        cont += 1
    print('-' * 20)