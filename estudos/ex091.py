from random import randint
from time import sleep
from operator import itemgetter #importante
jogadores = dict()
ranking = list()
print("Valores Sorteados:")
sleep(1)
for c in range (1,5):
    jogadores[f"jogador{c}"] = randint(1,6)
    print(f" -- O {f"jogador{c}"} tirou {jogadores[f"jogador{c}"]}")
    sleep(1)
print('-=-='*13) 
print('Ranking Jogadores:')
sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse = True)#se for zero ordem de chave, e se for 1 ordem de valor
ct = 1
for v in ranking:
    print(f'   {ct}° lugar: {v[0]} com {v[1]}')
    ct += 1
    sleep(1)