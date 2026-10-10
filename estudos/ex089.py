# essa foi minha 2° resolução
# dados = [[],[]]
# media = list()
# axl = list()
# while True:
#     nome = str(input('Qual nome ? '))
#     axl.append(float(input('Qual a 1° nota? '))) 
#     axl.append(float(input('Qual a 2° nota? ')))
#     media.append((axl[0]+axl[1])/2)
#     dados[0].append(nome)
#     dados[1].append(axl[:])
#     axl.clear()
#     ct = input('Quer continuar ? ')[0].upper()
#     if ct == 'N':
#         break
# print('-='*30)
# print('No. Nome         Média')
# print('-'*30)
# for c in range(0,len(dados[0])):
#     print(f'{c}   {dados[0][c]:<12} {media[c]:>}')
# print('-'*30)
# while True:
#     revisao = int(input('Quer ver as notas de qual aluno ? [999 stop]: '))
#     if revisao == 999:
#         break
#     print(f'As notas de {dados[0][revisao]} foram {dados[1][revisao]}')
# print('-='*30)
# print(f'<-------- Fim -------->')


# essa foi minha 1° resolução
'''lista = list()
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
print(f'-=-=-=-= < Volte Sempre! > -=-=-=-=')'''

#outra solução
dados = list()
cto = 0
while True:
    nome = str(input('Qual nome ? '))
    nota1 = float(input('Qual a 1° nota: '))
    nota2 = float(input('Qual a 2° nota: '))
    media = (nota1 + nota2)/2
    dados.append([nome, [nota1, nota2], media])
    cto += 1
    ct = input('Quer continuar ? ')[0].upper()
    if ct == 'N':
        break
print('-='*30)
print('No. Nome         Média')
print('-'*30)
for c in range(0,cto):
    print(f'{c}   {dados[c][0]:<12} {dados[c][2]:>}')
print('-'*30)
while True:
    revisao = int(input('Quer ver as notas de qual aluno ? [999 stop]: '))
    if revisao == 999:
        break
    if revisao <= len(dados)-1:
        print(f'As notas de {dados[revisao][0]} foram {dados[revisao][1]}')
        print('-'*30)
print(f'<-------- FIM -------->')