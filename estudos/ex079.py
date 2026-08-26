num = list()
while True:
    num.append(int(input('Digite um valor: ')))
    if num[-1] in num[0:(len(num)-1)]:
        num.pop()
        print('Valor duplicado! Não foi adicionado')
    else:
        print('Valor adicionado com sucesso')
    s = input('Quer continuar? ').upper().strip()[0]
    if s in 'Nn':
        break
print('-='*17)
num.sort()
print(f'Você digitou os valores {num}')#aqui poderia usar sorted(num)

#outra forma
'''
n = int(input(digite um valor))
if n not in num:
    num.append(n)
    print('Valor adicionado')
else:
    print('valor duplicado')
'''