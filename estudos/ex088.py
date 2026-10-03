from random import sample
from time import sleep
lista = list()
jogos = int(input('Quantos jogos você quer sortear? '))
sleep(1)
print(f'-=-=-=-= sorteando {jogos} jogos -=-=-=-=')
sleep(1)
for jogo in range(0,jogos):
    lista.append(sample(range(1,61),6))
    print(f'Jogo {jogo+1}: {sorted(lista[jogo])}')
    sleep(1)
print(f'-=-=-=-= < Boa sorte! > -=-=-=-=')

