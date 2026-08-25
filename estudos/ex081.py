num = []
while True:
    num.append(int(input('Digite um valor: ')))
    p = input('Quer continuar? ').strip().upper()[0]
    if p == 'N':
        break
print(f'Foram digitados {len(num)}')
num.sort(reverse=True)
print(f'A ordem decrescente é {num}')
if 5 in num:
    print('O Valor 5 foi digitado')
else:
    print('O valor 5 não foi digitado')