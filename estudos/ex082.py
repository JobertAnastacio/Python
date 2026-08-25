num = list()
par = list()
impar = list()
while True:
    num.append(int(input('Digite um valor: ')))
    l = input('Quer continuar [S/N]: ').strip()[0]
    if l in 'Nn':
        break
for p in range(0,len(num)):
    if num[p] % 2 == 0:
        par.append(num[p])
    else:
        impar.append(num[p])
print('-=-='*15)
print(f'A lista completa é {num}')
print(f'Os numeros pares são: {par}')
print(f'Os numeros impares são: {impar}')