#desafio 73
# criar tupla 20 primeiros colocados tabela do campeonato brasileiro na ordem de colocacao
#5 primeiro colocados
#ultimos 4 colocados
#times na ordem alfabetica
# em que posicao na tabela esta chapecoense

time =('atletico - mg','flamengo','palmeiras','fortaleza','corinthias',
       'bragantino','fluminense','america-mg','atletico-go','santos','ceara',
       'inernacional','sao paulo','atletico-pr','cuiaba','juventude','gremio','bahia','sport','chapecoense')

print('****'*20)
print('{:-^70}'.format('Campeonato Brasileiro'))
print('Os 5 primeiro colocados são : {}'.format(time[:5]))
print('---'*20)
print(f'Os 4 ultimos colocados são : {time[-4:]}')
print('---'*20)
print(f'Ordem alfabética  :{sorted(time)}')
print('---'*20)
print(f'o chapecoense está na {time.index("chapecoense")+1} °posicao ')
