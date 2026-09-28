# imcompleto falta B e C
m0 = list()
m1 = list()
m2 = list()
axl = list()
matriz = list()
pares = 0
while True:
    for o in range(0,3):
        axl.append(int(input(f'Digite um valor para [0,{o}]: ')))
        if axl[0] % 2 == 0:
            pares += axl[0]
        m0.append(axl[:])
        axl.clear()
    matriz.append(m0[:])
    for o in range(0,3):
        axl.append(int(input(f'Digite um valor para [0,{o}]: ')))
        if axl[0] % 2 == 0:
            pares += axl[0]
        m1.append(axl[:])
        axl.clear()
    matriz.append(m1[:])
    for o in range(0,3):
        axl.append(int(input(f'Digite um valor para [0,{o}]: ')))
        if axl[0] % 2 == 0:
            pares += axl[0]
        m2.append(axl[:])
        axl.clear()
    matriz.append(m2[:])
    break

print('-=-='*15)
print(f'A soma dos valores pares foi: {pares}')
print('-=-='*15)
