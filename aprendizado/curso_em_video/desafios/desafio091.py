# Crie um programa onde 4 JOGADORES joguem um "dado" e tenham resultados
# "aleatórios". Guarde esses resultados em um DICIONÁRIO. No final, coloque
# esse dicionário em "ordem", sabendo que o vencedor tirou o maior número no
# dado.

# SOLUÇÃO DO PROFESSOR:

from random import randint
from time import sleep
from operator import itemgetter

ranking = []
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

# Abaixo temos o método para organizar os elementos em ORDEM CRESCENTE
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')

for i, v in enumerate(ranking):
    print(f'   {i+1}º Lugar: {v[0]} com {v[1]}.')
    sleep(1)
