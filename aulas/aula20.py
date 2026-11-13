# def lin():
#     print('--'*15)
# # duas linhas da função para o programa principal

# lin()
# print('      sistema de alunos')
# lin()

# def titulo(msg):
#     print('--'*15)
#     print(msg)
#     print('--'*15)

# titulo('     Sistema de alunos')
# titulo('     Sistema de compras')

# def soma(a,b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma de {a} + {b} = {s}')

# lin()
# soma(3,4)
# lin()
# soma(6,9)
# lin()
# soma(b=2,a=6)
# lin()

# def contador(*núm):
#     tam = len(núm)
#     for valor in núm:
#         print(f'{valor} ', end='')
#     print('=> fim')
#     print(f'Recebi alguns valores, eles são ao todo {tam} numeros')

# contador(2,6,4,8,9)
# contador(1,0,5)
# contador(2,6,0,8,9,20)
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [7,5,6,7,8,3,4]
dobra(valores)
print(valores)


def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'somando os valores {valores} temos {s}' )


soma(9,5,7)
soma(1,3,4)