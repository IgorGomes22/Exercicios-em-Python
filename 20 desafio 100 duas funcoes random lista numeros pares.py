#desafio 100
#lista chamada numeros
#duas funcoes chamadas sorteio() e somaPar()
#a primeira funcao vai srtear 5 numeros e colocardentro da lista
#e a segunda funcao vai mostrar a soma entre todos os valores Pares
#sorteados pela funcao

from random import randint
from time import sleep

numeros = list()

def sorteio(lista):

    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f' {n} ',end='' , flush=True)
        sleep(0.3)
    print('Pronto')

def somaPar(lista):
    soma= 0
    for valor in lista:
        if valor %2 == 0:
            soma +=valor
    print(f'Somando os valores pares de{lista}, temos {soma}')
   
sorteio(numeros)
somaPar(numeros)

