# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()
ordem = nome.split()
print('Seu primeiro nome é: {}'.format(ordem[0]))
print('Seu último nome é: {}'.format(ordem[-1]))
