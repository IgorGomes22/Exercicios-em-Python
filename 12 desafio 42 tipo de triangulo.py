#desafio 42
# que tipo de triangulo sera formado
#ler tres valores e informar:
#equilatero :todos os lados iguais
#isosceles : dois lados iguais
#Escaleno : todos os lados diferentes

set =1
while   set ==True :
    print('==========tipos de triangulos=============')
    print('Insira os valores em para descobrir')
    n1 = int(input('primeiro valor :'))
    n2 = int(input('segundo valor :'))
    n3 = int(input('terceiro valor :'))
    if n1== 0 and n2==0 and n3 == 0:
       print('não é um triangulo')
    elif n1 == n2 and n1 == n3 :
       print('triangulo Equilatero')
    elif n1 == n2  or n1 == n3 or n2 == n3:
       print('Triangulo Isoceles ')
    elif  n1  != n2 and n1 != n3 and n2 != n3 :
       print('Triangulo Escaleno')
