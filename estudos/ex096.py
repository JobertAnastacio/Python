def area(l,c):
    area = l*c
    print(f'A área de um terreno {l}x{c} é de {area}m²')


print('   Controle de terrenos')
print('--'*15)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura,comprimento)