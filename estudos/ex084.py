teste = list()
dados = list()
pesado = list()
leve = list()
cont = 0
while True:
    teste.append(str(input('Digite seu nome: ')))
    teste.append(float(input('Digite seu peso: ')))
    cont += 1
    dados.append(teste[:])
    teste.clear()
    c = input('Quer continuar? ').strip().upper()[0]
    if c == 'N':
        break
for peso in dados:
    if peso[1] >= 100:
        pesado.append(peso[0])
    if peso[1] <= 60:
        leve.append(peso[0])
print(f'Foram cadastradas {cont} pessoas')
print(f'As pessoas com mais de 100 kg foram:{pesado}')
print(f'As pessoas com menos de 60kg foram: {leve}')

