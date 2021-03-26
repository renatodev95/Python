# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas
# respectivas posições na lista.

num = []
for c in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {c}: ')))
for p, v in enumerate(num):
    if p == 0:
        maior = v
        menor = v
    else:
        if v > maior:
            maior = v
        if v < menor:
            menor = v
print(f'Você digitou os valores {num}')
print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for p, v in enumerate(num):
    if v == maior:
        print(f'{p}... ', end='')
print(f'\nO menor valor digitado foi {menor} nas posições', end=' ')
for p, v in enumerate(num):
    if v == menor:
        print(f'{p}... ', end='')
