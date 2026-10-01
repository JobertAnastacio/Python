# imcompleto falta B e C
m0 = list()
m1 = list()
m2 = list()
axl = list()
matriz = list()
pares = col3 = maiorv = 0
while True:
    for o in range(0,3):
        axl.append(int(input(f'Digite um valor para [0,{o}]: ')))
        if axl[0] % 2 == 0:
            pares += axl[0]
        if o == 2:
            col3 += axl[0]
        m0.append(axl[:])
        axl.clear()
    matriz.append(m0[:])
    for o in range(0,3):
        axl.append(int(input(f'Digite um valor para [0,{o}]: ')))
        if o == 0:
            maiorv = axl[0]
        else:
            if axl[0] > maiorv:
                maiorv = axl[0]
        if axl[0] % 2 == 0:
            pares += axl[0]
        if o == 2:
            col3 += axl[0]
        m1.append(axl[:])
        axl.clear()
    matriz.append(m1[:])
    for o in range(0,3):
        axl.append(int(input(f'Digite um valor para [0,{o}]: ')))
        if axl[0] % 2 == 0:
            pares += axl[0]
        if o == 2:
            col3 += axl[0]
        m2.append(axl[:])
        axl.clear()
    matriz.append(m2[:])
    break

print('-=-='*15)
print(f'[ {matriz[0][0]} ][ {matriz[0][1]} ][ {matriz[0][2]} ]', end='')
print(f'\n[ {matriz[1][0]} ][ {matriz[1][1]} ][ {matriz[1][2]} ]', end='')
print(f'\n[ {matriz[2][0]} ][ {matriz[2][1]} ][ {matriz[2][2]} ]', end='')
print('\n')
print('-=-='*15)
print(f'A soma dos valores pares foi: {pares}.')
print(f'A soma dos valores da 3° coluna foi {col3}.')
print(f'O maior valor da segunda linha foi {maiorv}.')
print('-=-='*15)
