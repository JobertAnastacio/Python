teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Lucas'
teste[1] = 12
galera.append(teste[:])
print(galera)