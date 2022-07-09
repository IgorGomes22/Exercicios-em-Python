#desafio 68
# par ou impar
#so sera interrompido quando o jogador perder
#mostrando o total de vitorias conscutivas
from random import randint
soma=0
count = 0
while True :
    print('****'*10)
    print('--------Vamos Jogar Par ou Impar----------')
    computador = randint(0,10)
    print(computador)
    n1 = int(input('DIgite um numero:  '))
    soma = n1 + computador
    tipo = ' '
    print(computador)
    while tipo not in 'PI' :
        #strip elimina espaco antes e depois da frase, [0] pega  a 1°letra
        tipo = str(input('Par ou Ìmpar?  [P/I]')).strip().upper()[0] 
    print('Voce jogou {} e o computador {} . Total de   {} .'.format(n1,computador,soma))

    if tipo == 'P' :
        if soma % 2 ==0 :
           print('*********Voce Venceu********')
           count += 1
        else :
               print('**********Voce perdeu********')
               break
    elif tipo == 'I' :
        if soma % 2 == 1 :
            print('*********Voce Venceu********')
            count += 1
        else :
             print('**********Voce perdeu********')
             break
    print('++++++ Vamos jogar novamente ...+++++++')
     
print(f'Game Over ! Voce venceu {count} vezes')
        
