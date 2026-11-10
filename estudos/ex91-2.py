from operator import itemgetter
nomes = dict()
ranking = dict()
ct = 1
while True:
    nomes[f"pessoa{ct}"] = str(input('Digite seu nome: '))
    cont = input('Quer continuar?').upper()[0]
    print('---'*10)
    ct += 1
    if cont == 'N':
        break
ranking = sorted(nomes.items(), key = itemgetter(1))
n=1
for v in ranking:
    print(f'{n}° = {v[1]}')
    n +=1