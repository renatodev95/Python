# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nota1 = float(input('Informe a primeira nota do aluno: '))
nota2 = float(input('Informe a segunda nota do aluno: '))
media = (nota1+nota2) / 2
if media <= 7:
    print('A média do aluno foi {:.1f}. REPROVADO!'.format(media))
else:
    print('A média do aluno foi {:.1f}. APROVADO!'.format(media))
