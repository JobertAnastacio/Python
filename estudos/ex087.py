'''m0 = list()
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
print('-=-='*15)'''
# essa acima foi minha primeira solução
matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = col3 = maior = 0
for l in range(0,3):#linhas
    for c in range(0,3):#colunas
        matriz[l][c] = int(input(f'Digite um valor para {[l]},{[c]}: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if c == 2:
            col3 += matriz[l][c]
        if l == 1 and maior == 0:
            maior = matriz[l][c]
        else:
            if l == 1 and matriz[l][c] > maior:
                maior = matriz[l][c]
print('-=-='*15)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
    print()
print('-=-='*15)
print(f'A soma dos valores apres é {par}')#a
# outra forma de fazer a 'b' seria
'''
for l in range(0,3):
    col3 += matriz[l][2]'''
print(f'A soma dos valores da 3° coluna é {col3}')#b
# outra forma de fazer a 'c' seria
'''
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]'''
print(f'O maior valor da 2° linha é {maior}')#c