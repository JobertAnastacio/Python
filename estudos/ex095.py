dados = dict()
jogadores = list()
ngols = list()#lista para numero de gols por partida
ctjoga = 0 #contador jogadores pode ser len(jogadores)
while True:
    axl = 0
    ct = 0 #pode ser sum(ngols)
    dados['nome'] = input('Nome do Jogador: ')
    partidas = int(input(f'Quantas partidas {dados['nome']} jogou? '))
    for c in range(0,partidas):
        axl = int(input(f'Quantos gols na {c+1}° partida ? '))
        ct += axl
        ngols.append(axl)
    dados['gols'] = ngols[:]
    ngols.clear()
    dados['total'] = ct
    jogadores.append(dados.copy())
    ctjoga += 1
    continuar = input('Quer continuar [S/N]: ').strip().upper()[0]
    print('-=-='*10)
    if continuar == 'N':
        break
print('Cod. ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('----'*10)
for k,v in enumerate(jogadores):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('----'*10)
while True:
    mostrar = int(input('Mostrar dados de qual jogador? '))
    while mostrar > ctjoga:
        print(f'ERRO! Não existe jogador {mostrar}, tente novamente')
        print('----'*10)
        mostrar = int(input('Mostrar dados de qual jogador? '))
    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[mostrar]['nome']}: ')
    for i, gols in enumerate(jogadores[mostrar]['gols']):
        print(f'    Na partida {i+1}, fez {gols} gols.')
        
    continuar = input('Quer continuar [S/N]: ').upper()[0]
    if continuar == 'N':
        break
    print('----'*10)
print('====== FIM =====')
