# Aprimore o DESAFIO093 para que ele funcione com vários jogadores, incluindo
# um sistema de visualização de detalhes do aproveitamento de cada jogador.

aprov = {}
laprov = []
while True:
    print('—'*40)
    aprov['nome'] = str(input("Nome: "))
    partidas = int(input(f'Quantas partidas {aprov["nome"]} jogou? '))
    gols = []
    totgols = 0
    for c in range(partidas):
        gols.append(int(input(f"Quantos gols na partida {c}? ")))
        totgols += gols[c]
    aprov['gols'] = gols[:]
    aprov['total'] = totgols
    laprov.append(aprov.copy())
    gols.clear()
    resp = str(input("Quer continuar?[S/N] "))
    if resp in 'Nn':
        break
print('=-='*15)
print(f'{"Cod":<4}{"Nome":<10}{"Gols":<10}{"total":>10}')
print('—'*40)
for c in range(len(laprov)):
    print(f'{c:<4}{laprov[c]["nome"]:<10}', end=' ')
    print(f'{laprov[c]["gols"]}{laprov[c]["total"]:>10}')
    print()
while True:
    indice = int(input("Mostrar dados de qual jogador? "))
    if indice == 999:
        break
    if indice >= len(laprov):
        print(f'ERRO! Não existe jogador com código {indice}!')
    else:
        print(f'— LEVANTAMENTO DO JOGADOR {laprov[indice]["nome"]}:')
        for i, g in enumerate(laprov[indice]['gols']):
            print(f'No jogo {i+1} fez {g} gols.')
    print('—'*40)
print('<< VOLTE SEMPRE >>')
