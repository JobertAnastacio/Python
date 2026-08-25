#imcompleto
num = list()
for val in range(0,5):
    num.append(int(input('Digite um valor: ')))
    for n in range(0,len(num)):
        if num[val] > num[n]:
            num.insert(num[-1],num[val])
            num.pop()
        if num[val] < num[n]:
            num.insert(num[0],num[val])
            num.pop()
print(num)        