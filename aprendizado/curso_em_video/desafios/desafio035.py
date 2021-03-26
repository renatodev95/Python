# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('=-=' * 10)
print('ANALISADOR DE TRIÂNGULOS')
print('=-=' * 10)
ladoA = float(input('Primeiro segmento: '))
ladoB = float(input('Segundo segmento: '))
ladoC = float(input('Terceiro segmento: '))
if ladoA < ladoB+ladoC and ladoB < ladoA+ladoC and ladoC < ladoA+ladoB:
    print('Os sementos acima PODEM FORMAR um triângulo!')
else:
    print('Os sementos acima NÃO PODEM FORMAR um triângulo!')
