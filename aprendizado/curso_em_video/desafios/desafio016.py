# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
import math
numero = float(input('Digite um número: '))
parteInteira = math.trunc(numero)
print('O número {} te a parte inteira {}'.format(numero, parteInteira))
