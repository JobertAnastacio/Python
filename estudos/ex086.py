# m0 = list()
# m1 = list()
# m2 = list()
# matriz = list()
# while True:
#     for o in range(0,3):
#         m0.append(int(input(f'Digite um valor para [0,{o}]: ')))
#     matriz.append(m0[:])
#     for o in range(0,3):
#         m1.append(int(input(f'Digite um valor para [1,{o}]: ')))
#     matriz.append(m1[:])
#     for o in range(0,3):
#         m2.append(int(input(f'Digite um valor para [2,{o}]: ')))
#     matriz.append(m2[:])
#     break

# print('-=-='*15)
# print(f'[ {matriz[0][0]} ][ {matriz[0][1]} ][ {matriz[0][2]} ]', end='')
# print(f'\n[ {matriz[1][0]} ][ {matriz[1][1]} ][ {matriz[1][2]} ]', end='')
# print(f'\n[ {matriz[2][0]} ][ {matriz[2][1]} ][ {matriz[2][2]} ]', end='')

# essa de cima foi minha primeirta solução

'''matriz = [[],[],[]]
axl = 0
for c in range(0,3):
    axl = int(input(f'Digite um valor para [0,{c}]: '))
    matriz[0].append(axl)
for c in range(0,3):
    axl = int(input(f'Digite um valor para [1,{c}]: '))
    matriz[1].append(axl)
for c in range(0,3):
    axl = int(input(f'Digite um valor para [2,{c}]: '))
    matriz[2].append(axl)
print('-=-='*15)
print(f'[{matriz[0][0]}] [{matriz[0][1]}] [{matriz[0][2]}]')
print(f'[{matriz[1][0]}] [{matriz[1][1]}] [{matriz[1][2]}]')
print(f'[{matriz[2][0]}] [{matriz[2][1]}] [{matriz[2][2]}]')'''

# outro jeito mais simples

matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):#linhas
    for c in range(0,3):#colunas
        matriz[l][c] = int(input(f'Digite um valor para {[l]},{[c]}: '))
print('-=-='*15)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
    print()