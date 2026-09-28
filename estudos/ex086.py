m0 = list()
m1 = list()
m2 = list()
c = p = 0
while True:
    m0.append(int(input(f'Digite um valor para [{c},{p}]: ')))
    p +=1
    if p == 3:
        break
c = 1
p = 0
while True:
    m1.append(int(input(f'Digite um valor para [{c},{p}]: ')))
    p += 1
    if p == 3:
        break
c = 2
p = 0
while True:
    m2.append(int(input(f'Digite um valor para [{c},{p}]: ')))
    p += 1
    if p == 3:
        break
j = 0
for l in m0:
    print(f'[ {l} ]', end='')
print('\n')
for l in m1:  
    print(f'[ {l} ]', end= '')
print('\n')
for l in m2:
    print(f'[ {l} ]', end= '')    
