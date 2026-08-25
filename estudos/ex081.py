num = []
while True:
    num.append(int(input('Digite um valor: ')))
    p = input('Quer continuar? ').strip().upper()[0]
    if p == 'N':
        break
print('-=-='*12)
print(f'Foram digitados {len(num)} valores')
num.sort(reverse=True)
print(f'A ordem decrescente desses valores é: {num}')
if 5 in num:
    print('O Valor 5 foi digitado')
else:
    print('O valor 5 não foi digitado')