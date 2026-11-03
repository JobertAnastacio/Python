from random import randint
from time import sleep
jogadores = dict()
ranking = dict()
print("Valores Sorteados:")
for c in range (1,5):
    jogadores[f"j{c}"] = randint(1,6)
    print(f"   O {f"j{c}"} tirou {jogadores[f"j{c}"]}")
    sleep(1)
print('Ranking Jogadores:')
for v in jogadores.values():
    if jogadores["j1"] > v:
        ranking["j1"] = jogadores["j1"]
    elif jogadores["j2"] > v:
        ranking["j2"] = jogadores["j2"]
    elif jogadores["j3"] > v:
        ranking["j3"] = jogadores["j3"]
    elif jogadores["j4"] > v:
        ranking["j4"] = jogadores["j4"]
ct = 1
for k,v in ranking.items():
    print(f'   {ct}° lugar: {k} com {v}')
    ct += 1