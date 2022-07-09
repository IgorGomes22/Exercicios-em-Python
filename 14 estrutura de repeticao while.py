#  aula while
"""
set = 'S'
while set == 'S' :
    n = int(input('Digite um valor:  '))
    set = str(input('Quer continuar ?  [S/N]  ')).upper()
print('FIM')
"""

n = 1
par = impar = 0
while n  !=0  :
    n= int(input('Digite um valor  :'))
    if n != 0 :
        if n %2 == 0 :
            par += 1
        else :
            impar += 1
print('Voce digitou  {} numeros pares e {} numeros impares ! '.format(par,impar))
