termo = int(input('Digite o primeiro termo: '))
razão = int(input('Razão da PA: '))
c = 1
while c <= 10:
    print('{} ➡'.format(termo), end=' ')
    termo += razão
    c += 1
print('FIM')
