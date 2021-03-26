from random import randint
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior = menor = 0
print(f'O valores sorteados foram: {tupla}')
for cont in range(0, len(tupla)):
    if cont == 0:
        maior = tupla[0]
        menor = tupla[0]
    else:
        if tupla[cont] > maior:
            maior = tupla[cont]
        if tupla[cont] < menor:
            menor = tupla[cont]
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
