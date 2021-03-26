# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Informe o primeiro termo: '))
razão = int(input('Informe a razão da P.A: '))
decimo = termo + (11-1) * razão
for c in range(termo, decimo, razão):
    print('{}'.format(c), end=' -> ')
print('ACABOU')
