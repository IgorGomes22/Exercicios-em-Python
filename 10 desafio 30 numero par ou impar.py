#desafio 30
#leia um numero e mostre se e par ou impar

num= int(input('Digite um numero : '))
resto = num %2

if resto == 0:
         print('O Numero {}  é par '.format(num))
else :
    print('O numero {} é impar'.format(num))
