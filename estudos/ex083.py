# minha solução
parent1 = parent2 = 0
p = (input('Digite uma expresão para verificar se ela é válida: '))
for var in range(0,len(p)):
    if p[var] == '(':
        parent1 += 1
    if p[var] == ')':
        parent2 += 1
if parent1 == parent2:
    print('Expressão valida')
else:
    print('Expresão invalida')
# outra forma:
'''
simb = lis()
p = (input('Digite uma expresão para verificar se ela é válida: '))
for var in p:
    if var == '(':
        simb.append('(')
    elif var == ')':
        if len(simb) > 0:
            simn.pop()
        else:
            simb.append(')')
            break
if len(simb) == 0:
    print('Expressão valida')
else:
    print('Expresão invalida')
'''
