# o código em cometario foi minha resolução
# teste = list()
# total = list()
# par = list()
# impar= list()
#usando apenas uma lista fica assim
teste = 0
total =[[],[]]
for num in range(0,7):
    teste = int(input(f'Digite o {num+1}° numero: '))
    if teste % 2 == 0:
        total[0].append(teste)
    else:
        total[1].append(teste) 
    # teste.clear()
# total.append(par)
# total.append(impar)
print('-='*20)
print(f'Os numeros pares digitados foram {sorted(total[0])}')
print(f'Os numeros impares digitados foram {sorted(total[1])}')
    