#desafio 76
#tupla com nomes de produtos e seus precos na sequencia
#mostrar listagem de precos organizando os dados em forma tabular

listagem = ('carne',34.00,'frango',15.90,'carvao',20.00,'espeto',10.90,'guarana',10.00)

print('-' *30)
print(f'{"LISTAGEM DE PRECOS ":^40}')
print('-'*30)

for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end=' ')
    else:
        print(f'R${listagem[pos]:.>7.2f}')

print('-' *30)
 
