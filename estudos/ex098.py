from time import sleep

def linha():
    print('--'*15)

def contagem1(a,b,c):
    if a < b:
        if c == 0:
            c = 1
        print(f'Contagem de {a} até {b-1} de {c} em {c}')
        for cont in range(a,b,c):
            print(cont, end=' ')       
            # sleep(0.5)
        print('FIM!')

    else:
        if c < 0:
            c *= -1
        elif c == 0:
            c = 1
        print(f'Contagem de {a} até {b} de {c} em {c}')
        for cont in range(a,b-1,-c):
            print(cont, end=' ')       
            # sleep(0.5)
        print('FIM!')


linha()    
contagem1(1,11,1)
linha()
contagem1(10,0,2)
linha()
print('Agora sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
linha()
contagem1(inicio,fim,passo)

