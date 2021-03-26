from math import sin, cos, tan, radians
angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de {:.1f}° tem o seno de {:0.2f}'.format(angulo, seno))
print('O ângulo de {:.1f}° tem o coseno de {:0.2f}'.format(angulo, cosseno))
print('O ângulo de {:.1f}° tem a tangente de {:0.2f}'.format(angulo, tangente))

