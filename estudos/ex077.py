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

#outra forma mais simples de fazer o mesmo que o código acima
'''for p in palavras:
    print(f'\n{p.upper()} temos: ',end=' ')
    for vogal in p:
        if vogal.lower() in 'aeiou':
            print(vogal,end=' ')'''
