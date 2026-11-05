# incompleto
from random import randint
from time import sleep
jogadores = dict()
ranking = dict()
print("Valores Sorteados:")
for c in range (1,5):
    jogadores[f"jogador{c}"] = randint(1,6)
    print(f"   O {f"jogador{c}"} tirou {jogadores[f"jogador{c}"]}")
    # sleep(1)
print('Ranking Jogadores:')

for v in jogadores.values():
    for c in range(1,5):#descobrir o maior
        if jogadores[f"jogador{c}"] > v:
            ranking["jogador4"] = jogadores[f"jogador{c}"]  
            
for c in range(1,5):
    if jogadores[f"jogador{c}"] < jogadores["jogador1"]:
        ranking["jogador2"] = jogadores[f"jogador{c}"]

for c in range(1,5):
    if jogadores[f'jogador{c}'] < jogadores["jogador1"] and jogadores[f'jogador{c}'] < jogadores["jogador2"]:
            ranking['jogador3'] = jogadores[f'jogador{c}']
            
for v in jogadores.values():
    for c in range(1,5):#descobrir o menor
        if jogadores[f"jogador{c}"] < v:
            ranking["jogador4"] = jogadores[f"jogador{c}"]  
ct = 1
for k,v in ranking.items():
    print(f'   {ct}° lugar: {k} com {v}')
    ct += 1
    # sleep(1)