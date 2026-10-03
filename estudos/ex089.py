lista = list()
nomes = list()
notas = list()
media = list()
axl = list()
ct = 0
while True:
    nomes.append(str(input('Nome: ')))
    axl.append(float(input('Nota 1: ')))
    axl.append(float(input('Nota 2: ')))
    notas.append(axl[:])
    media.append((axl[0]+axl[1])/2)
    axl.clear()
    ct += 1
    c = input('Quer continuar? ').strip().upper()[0]
    if c == 'N':
        break
lista.append(nomes)
lista.append(notas)
lista.append(media)
print('-=-='*10)
print('No. NOME          MÉDIA')
print('---'*10)
for bole in range(0,ct):
    print(f'{bole}   {lista[0][bole]:<9}     {lista[2][bole]}')
    # poderia usar tbm nomes[bole] media[bole]
print('---'*10)
while True:
    p = int(input('Quer ver as notas de qual aluno? [999 Para]: '))
    if p == 999:
        break
    print(f'As Notas de {lista[0][p]} foram {lista[1][p]}')
    print('---'*10)
print('---'*10)
print(f'-=-=-=-= < Volte Sempre! > -=-=-=-=')  