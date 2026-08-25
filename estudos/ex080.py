num = list()
for val in range(0,5):
    num.append(int(input('Digite um valor: ')))
    for n in range(0,len(num)):
        if num[-1] < num[n]:
            num.insert(num[n],num[-1])
            num.pop()
        elif num[-1] > num[n]:
            num.insert(num[n],num[-1])
            num.pop()
        elif num[-1] < num[0]:
            num.insert(num[-1],num[0])
            num.pop(0)
    print(f'adicionado na posição {n}')
print(num)