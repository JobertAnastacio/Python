tabela = ('Palmeiras', 'Flamengo', 'CA-Paranaense', 'Fluminence', 'Bahia', 'Bragantino', 'Cruzeiro', 'Botafogo',
          'Corinthians', 'Atletico-Mineiro', 'Coritiba', 'São-Paulo', 'Vitória', 'Mirassol', 'Santos', 'Internacional',
          'Gremio', 'Vasco', 'Remo', 'Chapecoense')
while True:
    num = int(input('Quantos colocados você quer ver ? '))
    for pos,posicao in enumerate(tabela):
        print(f'Os {num} primeiros colocados são {posicao} {pos+1}° colocado')
        if pos == (num-1):
            break
    print('-=' * 30)
    co = 0
    l = 16
    for pos,posicao in enumerate(tabela):
        print(f'Os {l+1}° colocado é {tabela[l]}')
        l += 1
        co += 1
        if co == (4):
            break
    print('-=' * 30)
    print(sorted(tabela))
    print('-=' * 30)
    time = str(input('Qual time vc quer ver ? '))
    for pos,posicao in enumerate(tabela):
        if posicao == time:
            print(f'O {posicao} está em {pos+1}° Lugar')
            break
    break