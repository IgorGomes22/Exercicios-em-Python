#desafio 35
#comprimento de 3 retas se forma triangulo

print('-----Vamos ver se formamos um triangulo? -----')

a = int(input('DIgite o primeiro valor :'))
b = int(input('Digite o segundo valor :'))
c = int(input('Digite o terceiro valor :'))

if a <=0 or b<=0 or c<=0:
        print('Valor invalido em um dos lados,devem ser maiores que 0')
        
elif    a+b > c     and   b+c> a   and   a+c> b :
    print(' {},{},{} ,formam um triangulo'.format(a,b,c))
else:
    print(' {},{},{} , não formam um triangulo'.format(a,b,c))
