#desafio 67
#tabuada de varios numeros,um de cada vez
#sera interrompido caso o numero for negativo



n2 = 0
while True :
    n1 = int(input('Quer ver a tabuada de qual valor ? '))
    print('----'*10)
    if n1 <0 :
        break
    for n2 in range (1,11):
          print( f'{n2} X {n1} = { n1*n2}')
    print('----'*10)
print('programa encerrado,volte sempre')
    
