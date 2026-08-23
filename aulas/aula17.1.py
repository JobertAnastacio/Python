valores = [] # ou valores = list()
'''for cont in range(0,5):
    valores.append(int(input('Digite um numero:')))
print('Os valores que você digitou são:')'''
'''for pos,v in enumerate(valores):
    print(f'O {pos+1}° é {v}...')'''

#situação
a = [1,2,3,4]
#aqui é feito uma ligação entre as listas
'''b = a '''
#para criar uma copia basta:
b = a[:]
b[2] = 10
print(f'A lista a: {a}')
print(f'A lista b: {b}')