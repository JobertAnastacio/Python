total = list()
teste = list()
par = list()
impar= list()
for num in range(0,7):
    teste.append(int(input(f'Digite o {num+1}° numero: ')))
    if teste[0] % 2 == 0:
        par.append(teste[:])
        
    else:
        impar.append(teste[:])
        
    teste.clear()
total.append(par)
total.append(impar)
print('-='*20)
print(f'Os numeros digitados foram {sorted(total)}')
print(f'Os numeros pares digitados foram {sorted(total[0])}')
print(f'Os numeros impares digitados foram {sorted(total[1])}')
    