from random import randint

def sorteia(lst):
    print('Sorteando valores da lista: ',end=' ')
    for num in lst:
        print(num, end=' ')
    print('FIM!')

def pares(list):
    pares = 0
    for c in list:
        if c % 2 == 0:
            pares += c
    print(f'A soma de todos os valores pares de {list} é {pares}')


numeros = [randint(1,10), randint(1,10), randint(1,10),randint(1,10), randint(1,10)]
sorteia(numeros)
pares(numeros)