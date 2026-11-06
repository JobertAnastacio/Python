dados = dict()
ngols = list()#lista para numero de gols por partida
axl = 0
ct = 0 #contador
dados['nome'] = input('Nome do Jogador: ')
partidas = int(input(f'Quantas partidas {dados['nome']} jogou? '))
for c in range(0,partidas):
    axl = int(input(f'Quantos gols na {c}° partida ? '))
    ct += axl
    ngols.append(axl)
dados['gols'] = ngols[:]
dados['total'] = ct
print('-=-='*10)
for k,v in dados.items():
    print(f'O campor {k} tem valor {v}.')
print('-=-='*10)
print(f'O jogador {dados['nome']} jogou {partidas} partidas')
for partida, gols in enumerate(ngols):
    print(f'==> Na partida {partida}, fez {gols} gols.')
print(f'Foi um total de {ct} gols')