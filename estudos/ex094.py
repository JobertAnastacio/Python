dados = dict()
cadastros = list()
mulheres = list()
totalpessoas = 0
ct = 0 #para somar as idades pra depois fazer a media
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
    dados['idade'] = int(input('Idade: '))
    ct += dados['idade']
    totalpessoas += 1
    cadastros.append(dados.copy())
    if dados['sexo'] == 'F':
        mulheres.append(dados['nome'])
    cont = input(('Quer continuar ? ')).upper()[0]
    if cont == 'N':
        break
medidade = ct/totalpessoas
print('-=-='*10)
print(f'- Foram cadastradas {totalpessoas} pessoas.')
print(f'- A média de idade foi {medidade:.2f}')
print(f'- As mulheres foram:', end=' ')
for c in mulheres:
    print(c, end=' ')
