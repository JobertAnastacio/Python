dados = dict()
jogadores = list()
ngols = list()#lista para numero de gols por partida
ctjoga = 0 #contador jogadores
while True:
    axl = 0
    ct = 0
    dados['nome'] = input('Nome do Jogador: ')
    partidas = int(input(f'Quantas partidas {dados['nome']} jogou? '))
    for c in range(0,partidas):
        axl = int(input(f'Quantos gols na {c}° partida ? '))
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
print(f'{'Cod':<} nome      {'gols'}    {'total':>}')
print('----'*10)
v = 0
for c in jogadores:
    print(f'{v}   {c['nome']}        {c['gols']}        {c['total']:>}')
    v += 1
print('----'*10)
while True:
    mostrar = int(input('Mostrar dados de qual jogador? '))
    while mostrar > ctjoga:
        print(f'ERRO! Não existe jogador {mostrar}, tente novamnete')
        print('----'*10)
        mostrar = int(input('Mostrar dados de qual jogador? '))
    print(f'--LEVANTAMENTO DO JOGADOR {jogadores[mostrar]['nome']}: ')
    vjogo = 0
    for gols in jogadores[mostrar]['gols']:
        print(f'    Na partida {vjogo}, fez {gols} gols.')
        vjogo += 1
    continuar = input('Quer continuar [S/N]: ').upper()[0]
    if continuar == 'N':
        break
    print('----'*10)
