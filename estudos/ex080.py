num = list()
for val in range(0,5):
    n = int(input('Digite um valor: '))
    if val == 0 or n > num[-1]:
        num.append(n)
        print('Adicionado no final da lista')
    else:
        l = 0
        while l < len(num):
            if n <= num[l]:
                num.insert(l,n)
                print(f'Adicionado na posição {l}')
                break
            l += 1
print(num)        