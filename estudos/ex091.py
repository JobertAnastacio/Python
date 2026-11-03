from random import randint
from time import sleep
jogadores = dict()
print("Valores Sorteados:")
for c in range (1,5):
    jogadores[f"jogador{c}"] = randint(1,6)
    print(f"   O {f"jogador{c}"} tirou {jogadores[f"jogador{c}"]}")
    sleep(1)
print('Ranking Jogadores:')
ranking = list()
for v in jogadores.values():
    
ct = 1
for k,v in jogadores.items():
    print(f'   {ct}° lugar: {k} com {v}')
    ct += 1