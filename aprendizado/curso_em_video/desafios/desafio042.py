# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

seg1 = int(input('Primeiro segmento: '))
seg2 = int(input('Segundo segmento: '))
seg3 = int(input('Terceiro segmento: '))
if seg1 < seg2+seg3 and seg2 < seg3+seg1 and seg3 < seg1+seg2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if seg1 != seg2 != seg3:
        print('ESCALENO!')
    elif seg2 == seg1 == seg3:
        print('EQUILÁTERO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM um triângulo.')
