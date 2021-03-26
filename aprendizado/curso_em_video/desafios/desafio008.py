# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
medida = float(input('Informe uma distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
ct = medida * 100
ml = medida * 1000
print('A medida de {:.1f}m corresponde a: \n{:.3f}Km \n{:.2f}hm \n{:.1f}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(medida, km, hm, dam, dm, ct, ml))
