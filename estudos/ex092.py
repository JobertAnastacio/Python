from datetime import date 
cadastro = dict()
anoatual = date.today().year
cadastro['nome'] = input('Digite seu nome: ').strip()
anopessoa = int(input('Digite seu ano de nascimento: '))
cadastro['idade'] = anoatual - anopessoa
carteira = int(input('Numero carteira de trabalho (0 Não tem): '))
if carteira == 0:
    cadastro['ctps'] = carteira
else:
    cadastro['ctps'] = carteira
    anocontrato = int(input('Digite o ano em que você foi contratado: '))
    cadastro['contrataçao'] = anocontrato
    cadastro['salario'] = float (input('Qual seu salário: R$'))
    cadastro['aposentadoria'] = (anocontrato+35)- anopessoa
print('-='*15)
for k,v in cadastro.items():
    print(f'{k} é igual a {v}')
#35 anos de colaboração