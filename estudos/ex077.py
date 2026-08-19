palavras = ('aprender', 'programar', 'linguagem', 'python','futuro','escola','lixo','casa','carro','computador')
for c in range(0,len(palavras)):
    print(f'\nNa palavra {palavras[c].upper()} temos: ',end=' ')
    for v in range(0,len(palavras[c])):
        if palavras[c][v] == 'a':
          print(palavras[c][v],end=' ')
        if palavras[c][v] == 'e':
          print(palavras[c][v],end=' ')
        if palavras[c][v] == 'i':
          print(palavras[c][v],end=' ')
        if palavras[c][v] == 'o':
          print(palavras[c][v],end=' ')
        if palavras[c][v] == 'u':
          print(palavras[c][v],end=' ')