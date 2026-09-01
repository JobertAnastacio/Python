pessoas = list()
dados = list()
maior = list()
menor = list()
quant = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso [KG]: ')))
    pessoas.append(dados[:])
    dados.clear()
    quant += 1
    c = input('Quer continuar? ').upper()[0]
    if c == 'N':
        break
for p in pessoas:
    if p[1] >= 100:
        maior.append(p[0])
    if p[1] <= 65:
        menor.append(p[0])

print(f'Foram cadastradas {quant} pessoas')
print(f'As pessoas mais pessadas (> 100 kg) foram : {maior[:]}')
print(f'As pessoas mais leves (< 65 kg) foram: {menor}')