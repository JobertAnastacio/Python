m0 = list()
m1 = list()
m2 = list()
matriz = list()
while True:
    for o in range(0,3):
        m0.append(int(input(f'Digite um valor para [0,{o}]: ')))
    matriz.append(m0[:])
    for o in range(0,3):
        m1.append(int(input(f'Digite um valor para [1,{o}]: ')))
    matriz.append(m1[:])
    for o in range(0,3):
        m2.append(int(input(f'Digite um valor para [2,{o}]: ')))
    matriz.append(m2[:])
    break

print('-=-='*15)
print(f'[ {matriz[0][0]} ][ {matriz[0][1]} ][ {matriz[0][2]} ]', end='')
print(f'\n[ {matriz[1][0]} ][ {matriz[1][1]} ][ {matriz[1][2]} ]', end='')
print(f'\n[ {matriz[2][0]} ][ {matriz[2][1]} ][ {matriz[2][2]} ]', end='')

