it = ('Cafe',7.00,'Leite',2.00,'Pão',5.55,'Feijão',4.00,'Açucar',2.00,'Arroz',4.90,'Macarrão',3.40,'Carne',24.90)
print('_'*40)
print(f'{'lista de produtos':^40}')
print('_'*40)
for c in range(0,len(it),2):
    print(f' {it[c]}............................R${it[c+1]}')
print('_'*40)