#desafio 106
#mini sistema usando interactive help
#o usuario vai digitar o comando e o manual aparecer
#quando usuario digitar a palavra 'fim',o programa encerra
#use cores
from time import sleep

c = ('\033[m',          # 0 sem cor
     '\033[0;30;41m',   # 1 vermelho
     '\033[0;30;42m',   # 2 verde
     '\033[0;30;43m',   # 3 amarelo
     '\033[0;30;44m',   # 4 azul
     '\033[0;30;45m',   # 5 roxo
     '\033[0;30'        # 6 branco
     );


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'',4)
    print(c[6],end='')
    help(com)
    print(c[0],end='')
    sleep(2)

    
def titulo(msg,cor=0):
    tam = len(msg) +4
    print(c[cor],end='')
    print('~'*tam)
    print(f'{msg}')
    print('~'*tam)
    print(c[0],end='')
    sleep(1)
    
comando =''
while True :
    titulo('SISTEMA DE AJUDA PyHelp',1)
    comando =str(input("Funcao ou biblioteca > "))
    if comando.upper() =='FIM':
        break
    else:
        ajuda(comando)
titulo('Ate logo' ,1)
