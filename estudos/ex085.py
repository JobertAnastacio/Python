par = list()
impar = list()
total = list()
teste = list()
for num in range(0,7):
    teste.append(int(input(f'Digite o {num+1}° numero:')))
    if teste[0] % 2 == 0:
        total.append(teste[:])
    else:
        total.append(teste[:])
    teste.clear()

print(f'Os numeros digitados foram {sorted(total)}')
print(f'Os numeros pares digitados foram {total[0]}')
print(f'Os numeros impares digitados foram {total[1]}')
    