from random import randint
from time import sleep
jogadores = {"jogador1":'',"jogador2": '', "jogador3": '',"jogador4": ''}
print("Valores Sorteados:")
for c in range (1,5):
    jogadores[f"jogador{c}"] = randint(1,6)
    print(f"   O {f"jogador{c}"} tirou {jogadores[f"jogador{c}"]}")
    sleep(1)