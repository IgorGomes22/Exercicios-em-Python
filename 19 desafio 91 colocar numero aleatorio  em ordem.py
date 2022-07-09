#desafio 91
#crie um programa 4 jogadores joguem 1 dado
#ter resultado aleatorio
#guardar resultado em um dicionario
#no final, colocar em ordem sabendo que o vencedor tirou o maior numero

from random import randint
from time import sleep
from operator import itemgetter

jogo = { 'jogador1' : randint(1,6),
              'jogador2': randint(1,6),
              'jogador3': randint(1,6),
              'jogador4': randint(1,6)}

ranking = dict()

print('-----------Valores sorteados-----------------')
for k,v in jogo.items():
    print(f' - O {k} tirou {v} no dado. ')
    sleep(1)
    
ranking = sorted(jogo.items(), key=itemgetter(1),reverse=True)
print('==============Ranking dos jogadores =============')
for i, v in enumerate(ranking):
    print(f' {i+1}° lugar : {v[0]} com {v[1]}.')
