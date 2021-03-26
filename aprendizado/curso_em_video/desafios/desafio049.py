num = int(input('Digite um número para ver sua tabuada: '))
print('TABUADA DE {}...'.format(num))
print('-='*10)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
print('-='*10)
