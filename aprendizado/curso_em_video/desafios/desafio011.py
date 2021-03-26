# Faça um programa que leia a largua e a altura de uma parede em metros, calcule a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
largura = float(input('Qual a largura da parede (em metros)? '))
altura = float(input('Qual a altura da parede (em metros)? '))
area = largura * altura
tinta = area / 2
print('A área da parede é de {}m² e a quantidade de tinta necessária para pintá-la é de {}l litros.'.format(area, tinta))
