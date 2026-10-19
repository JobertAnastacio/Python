dados = {'nome':'','media':'','situacao':''}
dados['nome'] = str(input('Nome: '))
dados['media'] = float(input(f'Média de {dados['nome']}: '))
if dados['media'] >= 7:
    dados['situação'] = 'Aprovado'
else:
    dados['situação'] = 'Reprovado'
print('-='*15)
print(f'O nome do aluno é {dados['nome']}')
print(f'Média é igual a {dados['media']}')
print(f'A situação dele é {dados['situação']}')