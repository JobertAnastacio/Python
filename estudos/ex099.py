def maior(lst):
    print('Analisando valores...')
    if len(lst) == 0:
        print(f'foram informados {len(lst)} valores')
        print(f'O maior valor foi 0')
    else:
        maiorv = lst[0]
        for c in lst:
            print(c, end =' ')
            if maiorv < c:
                maiorv = c
        print(f'foram informados {len(lst)} valores')
        print(f'O maior valor foi {maiorv}')

def linha():
    print('--'*15)

linha()
valores = [2,9,4,5,7,1]
maior(valores) 
linha()
valores = [4,7,0]
maior(valores)   
linha()
valores = [1,2]
maior(valores)  
linha()
valores = [6]
maior(valores) 
linha()
valores = []
maior(valores)  