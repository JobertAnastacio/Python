valores = list()
ct = maior = menor =  0
for val in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {val}: ')))
    if ct == 0:
        maior = valores[val]
        menor = valores[val]
    else:
        if valores[val] > maior:
            maior = valores[val]
        if valores[val] < menor:
            menor = valores[val]     
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