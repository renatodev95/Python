# Faça um programa que leia um número qualquer e mostre na tela a sua tabuada.
numero = int(input('Digite um número para ver sua tabuada: '))
c = 1
print('-' * 12)
while c <= 10:
    print('{} x {:2} = {}'.format(numero, c, numero*c))
    c += 1
print('-' * 12)
