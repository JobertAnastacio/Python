dados = dict()
cadastros = list()
mulheres = list()
acimamedia = list()
ct = 0 #para somar as idades pra depois fazer a media
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
    while dados['sexo'] not in 'MF':
        print('Por favor, digite apenas MASCULINO ou FEMININO')
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
    dados['idade'] = int(input('Idade: '))
    ct += dados['idade']
    cadastros.append(dados.copy())
    if dados['sexo'] == 'F':
        mulheres.append(dados['nome'])
    cont = input(('Quer continuar ? ')).upper()[0]
    while cont not in 'SN':
        print('Por favor, digite apenas SIM ou NÃO')
        cont = input(('Quer continuar ? ')).upper()[0]
    if cont == 'N':
        break
totalpessoas = len(cadastros)
medidade = ct/totalpessoas
print('-=-='*10)
print(f'- Foram cadastradas {len(cadastros)} pessoas.')
print(f'- A média de idade foi {medidade:5.2f}')
print(f'- As mulheres foram:', end=' ')
for c in mulheres:
    print(c, end=' ')
print()
print('A lista de pessoas que estão com a idade acima da média são: ')
for c in cadastros:
    if c['idade'] >= medidade:
        acimamedia.append(c)
for c in acimamedia:
     print(f'Nome = {c['nome']}, sexo = {c['sexo']}, idade = {c['idade']}')

# outra forma
# for c in cadastros:
#     if c['idade'] >= medidade:
#       print('   ', end='')
        # for k,v in c.items():
        #     print(f'{k} = {v}; ', end='')
        # print()
