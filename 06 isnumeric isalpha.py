# aqui vamos verificar se o valor digitado é numerico ou é string /verdadeiro ou falso

n1 = input('Digite algo n1:  ')
n2 = input('Digite algo n2:  ')

if n1.isnumeric() :
   print('n1  é um número')
else:
       print('n1 náo é numerico')
if n2.isalpha() :
    print('n2  é uma string')
else:
        print('n2 não é uma string')
