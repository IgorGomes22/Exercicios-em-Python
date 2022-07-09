#desafio 45
#criar um jogo que o computador jogue  jokenpo(pedra,papel,tesoura)

from random import randint
from time import sleep


itens = ('Pedra' , 'Papel' , 'Tesoura' )

computador = randint(0,2)
set = 1

while set ==1 :
        print('==='*11)
        print (""" suas opções :
        [0] Pedra
        [1] Papel
        [2] Tesoura """)

        jogador =int(input('Escolha sua jogada   '  ))
        if jogador >=  3 :
            print("""
>>>>>INSIRA UM VALOR VÁLIDO
""")
            continue
        print ('Jo')
        sleep (1)
        print('ken')
        sleep(1)
        print('pô')
        sleep(1)
        print(' ===' *11 )

        print (f'Computador jogou : {itens[computador]}'  )
        print (f' Jogador jogou : {itens[jogador]}' )
        

        if computador == 0 :
            if jogador == 0 :
                print('EMPATE')
            elif jogador == 1:
                print('JOGADOR VENCEU')
            elif jogador ==2 :
                print('COMPUTADOR VENCEU')
            else :
                print(' JOGADA INVALIDA')
                
        elif computador == 1 :
            if jogador == 0 :
                print('COMPUTADOR VENCEU')
            elif jogador == 1:
                print('EMPATE')
            elif jogador ==2 :
                print('JOGADOR VENCEU')
            else :
                print(' JOGADA INVALIDA')

        elif computador == 2:
            if jogador == 0 :
                print('JOGADOR VENCEU')
            elif jogador == 1:
                print('COMPUTADOR VENCEU')
            elif jogador ==2 :
                print('EMPATE')
                
        else   :
                print(' JOGADA INVALIDA')
                
  
