tabela = ('Palmeiras', 'Flamengo', 'CA-Paranaense', 'Fluminence', 'Bahia', 'Bragantino', 'Cruzeiro', 'Botafogo',
          'Corinthians', 'Atletico-Mineiro', 'Coritiba', 'São-Paulo', 'Vitória', 'Mirassol', 'Santos', 'Internacional',
          'Gremio', 'Vasco', 'Remo', 'Chapecoense')
while True:
    num = int(input('Quantos colocados você quer ver ? '))
    #verificando os primeiros 4 colocados
    print(f'Os {num} primeiros colocados são: ')
    for pos,time in enumerate(tabela):
        print(f'{time} {pos+1}° colocado')
        if pos == (num-1):
            break
    print('-=' * 30)
    co = 0
    l = 16
    #verificando os ultimos 4 colocados, poderia ser feito print(tabela[-4:])
    for pos,time in enumerate(tabela):
        print(f'Os {l+1}° colocado é {tabela[l]}')
        l += 1
        co += 1
        if co == (4):
            break
    #Olhando a ordem alfabetica
    print('-=' * 30)
    print(sorted(tabela))
    print('-=' * 30)
    #para ver a posição de um time especifico, poderia usar print(tabela.index('Palmeiras')+1) mas assim fica mais dinamico
    time1 = str(input('Qual time vc quer ver ? '))
    for pos,time in enumerate(tabela):
        if time == time1:
            print(f'O {time} está em {pos+1}° Lugar')
            break
    break