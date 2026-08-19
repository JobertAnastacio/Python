a = int(input('digite um valor: '))
b = int(input('digite um valor: '))
c = int(input('digite um valor: '))
d = int(input('digite um valor: '))
v = (a,b,c,d)
print(f'Você digitou os valores {v}')
print(f'O valor 9 aparece {v.count(9)} vezes')
#para verificar a posição do valor 3, poderia ser feito print(v.index(3)+1)
print('O valor 3 foi digitado primeiro na',end=' ')
for g in range(0,4):
    if v[g] == 3:
        print(f'{g+1}° Posição')
if 3 not in v:
    print('em nenhuma posição')
print('Os numeros pares foram: ',end='')
for l in range(0,4):
    if v[l] % 2 == 0:
     print(v[l],end=' ')

#outra forma de fazer a tupla
'''v = (int(input('Digite um valor: ')),
    int(input('Digite outro valor: ')),
    int(input('Digite mais um valor: ')),
    int(input('Digite o último valor: ')))
print(v)'''
