#desafio 88
#ajude o jogador da mega sena a criar palpites
#o programa pergunta quantos jogos serao gerados
#e sortear 6 numeros entre 1 e 60
#cadastrando tudo em uma lista

print('==='*20)
print('                                JOGO DA MEGA SENA               ')
print('==='*20)

from random import randint
from time import sleep

lista = list()
jogos = list()

quant = int(input('Quantos jogos voce quer que eu sorteie ? '))
tot = 1

while tot <= quant :
    cont = 0
    while True :
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6 :
            break 
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f' SORTEANDO {quant} JOGOS ' , '-='*3 )
for i , l in enumerate(jogos) :
    print(f' jogo {i +1}: {l} ')
    sleep(2)
print('-='*5 , '< BOA SORTE! >' , '-='*5)
