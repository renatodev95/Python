# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O
# programa vai ler o "nome do jogador" e quantas partidas ele jogou. Depois vai
# ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o
# campeonato.

aprov = {}
aprov['nome'] = str(input("Nome do jogador: "))
partidas = int(input(f'Quantas partidas {aprov["nome"]} jogou? '))
gols = []
totgols = 0
for c in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {c}: ')))
    totgols += gols[c]
aprov['gols'] = gols[:]
aprov['total'] = totgols

print('=-='*20)
print(aprov)
print('=-='*20)
for k, v in aprov.items():
    print(f'O campo {k} tem o valor {v}.')
print('=-='*20)
print(f'O jogador {aprov["nome"]} jogou {partidas} partidas.')
for i, j in enumerate(gols):
    print(f'    => Na partida {i}, fez {j} gols.')
print(f'Foi um total de {totgols} gols.')
