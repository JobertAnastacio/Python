from random import randint
from time import sleep
lista = list()
jogos = int(input('Quantos jogos você quer sortear? '))
sleep(1)
print(f'-=-=-=-= sorteando {jogos} jogos -=-=-=-=')
sleep(1)
for jogo in range(0,jogos):
    lista.append(f'{randint(1,60)}, {randint(1,60)}, {randint(1,60)}, {randint(1,60)}, {randint(1,60)}, {randint(1,60)}')
    print(f'Jogo {jogo+1}: [{lista[jogo]}]')
    sleep(1)
print(f'-=-=-=-= < Boa sorte! > -=-=-=-=')
