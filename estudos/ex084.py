teste = list()
dados = list()
pesado = leve = 0
while True:
    teste.append(str(input('Digite seu nome: ')))
    teste.append(float(input('Digite seu peso: ')))
    if len(dados) == 0:
        pesado = teste[1]
        leve = teste[1]
    else:
        if teste[1] > pesado:
            pesado = teste[1]
        if teste[1] < leve:
            leve = teste[1]
    dados.append(teste[:])
    teste.clear()
    c = input('Quer continuar? ').strip().upper()[0]
    if c == 'N':
        break

print(f'Foram cadastradas {len(dados)} pessoas')
print(f'As pessoas com mais de {pesado} kg foram:', end = ' ')
for pessoas in dados:
    if pessoas[1] == pesado:
        print(f'[{pessoas[0]}]',end = ' ')
print() #isso quebra a linha
print(f'As pessoas com menos de {leve} kg foram: ',end = ' ')
for pessoas in dados:
    if pessoas[1] == leve:
        print(f'[{pessoas[0]}]',end = ' ')
# outra forma usando pesado e leve como listas
# for peso in dados:
#     if peso[1] >= 89:
#         pesado.append(peso[0])
#     if peso[1] <= 60:
#         leve.append(peso[0])
