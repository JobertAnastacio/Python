galera = list()
dados = list() #estrutura auxiliar
mad = med = 0
for c in range (0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
print(galera)
for pessoa in galera:
    if pessoa[1] >= 18:
        print(f'{pessoa[0]} é maior de idade')
        mad += 1
    else:
        print(f'{pessoa[0]} é menor de idade')
        med +=1
print(f'O total de pessoas maior de idade foi {mad} e de pessoas menor de idade foi {med}')