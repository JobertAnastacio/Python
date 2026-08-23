valores = list()
ct = maior= menor = pp = pg =  0
for val in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {val}: ')))
for pos,v in enumerate(valores):
    if ct == 0:
        pg = pos
        pp = pos
        maior = v
        menor = v
    else:
        if v > maior:
            maior = v
            pg = pos
        if v < menor:
            menor = v
            pp = pos
    ct += 1
print(f'Os valores digitados foram {valores}')
print(f'O maior numero foi {maior} digitado nas posições',end=' ')
for pos,g in enumerate(valores):
    if maior == g:
        print(f'{pos}...',end=' ')
print(f'\nO menor foi {menor} digitado nas posições',end=' ')
for pos,p in enumerate(valores):
    if menor == p:
        print(f'{pos}...',end=' ')