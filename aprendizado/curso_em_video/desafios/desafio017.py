# Faça um programa que leia o comprimento do catero oposto e do cateto adjacente de um triangulo retângulo, calcule
# e mostre o comprimento da hipotenusa.
import math
catetoOposto = float(input('Informe o valor do cateto oposto: '))
catetoAdjacente = float(input('Informe o valor do cateto adjacente: '))
hipotenusa = math.hypot(catetoOposto, catetoAdjacente)
print('De acordo com os valores informados, o comprimento da hipotenusa é igual a: {:.2f}.'.format(hipotenusa))

