soma = 0
n = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        n += 1
print('A SOMA entre todos os {} NÚMEROS ÍMPARES que são MÚLTIPLOS DE TRÊS é igual a: {}'.format(n, soma))
