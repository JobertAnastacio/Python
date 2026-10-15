# pessoas = {'nome': 'Gustavo','Sexo': 'M','idade':22}
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
# pessoas['peso'] = 98.5
# print(pessoas.items())

# for k, v in pessoas.items():
#     print(f'{k} = {v}')

'''brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'uf': 'Ceará', 'Sigla': 'CE'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['Sigla'])'''

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)