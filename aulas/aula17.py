num = [2,5,9,1]
num[2] = 10
num.append(7)
num.insert(3,2)
if 2 in num:
    num.remove(2)
else:
    print('Não achei o valor 9')
num.remove(2)#elimina o primeiro valor que ele encontrar
#num.sort()
#num.pop(3)
#para ter os numeros ordenados em ordem inversa
#num.sort(reverse=True) 
print(num)
print(f'Essa lista tem {len(num)} elementos')