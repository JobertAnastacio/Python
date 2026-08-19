from random import choice
num = ( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
maior = menor = c = 0
print('Os valores sorteados foram: ', end='')
for es in num:
    b = choice(num)
    print(b, end=' ')
    c += 1
    if c == 1:
        maior = menor = b
    else:
        if b > maior:
            maior = b
        if b < menor:
            menor = b
    if c == 5:
        break

print('\n')
print(f'O maior valor foi {maior}')
print(f'o menor valor foi {menor}')

#outra forma de fazer o mesmo código é:

from random import randint
n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Os valores osrteados foram {n}')
print(f'O maior valor foi {max(n)}')
print(f'O menor valor foi {min(n)}')
