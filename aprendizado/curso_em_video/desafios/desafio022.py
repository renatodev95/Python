"""Crie um programa que leia o nome completo de uma pessoa e mostre: a)O nome com todas as letras maiúsculas;
 b)O nome com todas as letras minúsculas; c)Quantas letras no total (sem considerar ESPAÇOS);
 d)Quantas letras tem o primeiro nome."""

nome = str(input('Informe o seu nome completo: ')).strip()
print('Seu nome completo é {}.'.format(nome))
print('Seu nome em letras maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem um total de {} letras (desconsiderando os espaços).'.format(len(nome)-nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome tem {} letras.'.format(len(separa[0])))

