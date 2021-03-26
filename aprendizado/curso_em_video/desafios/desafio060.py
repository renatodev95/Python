f = int(input('Informe um número: '))
a, b = 1, 1
c = 1
print('Calculando {}!'.format(f))
while c <= f:
    f -= 1
    b = a
    a = b * c
    print(a)
print('= {}'.format(a))
