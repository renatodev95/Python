# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre
# seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura**2)
print('Seu IMC é: {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO ideal.')
elif imc <= 25:
    print('Parabéns, você está no seu PESO IDEAL.')
elif imc < 30:
    print('Tenha cautela, você está com SOBREPESO.')
elif imc <= 40:
    print('CUIDADO! Você está em situação de OBESIDADE!')
else:
    print('Cuidado, VOCÊ ESTÁ COM OBESIDADE MÓRBIDA!')
