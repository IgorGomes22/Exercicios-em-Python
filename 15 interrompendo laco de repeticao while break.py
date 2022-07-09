# aula 15 interrompendo repetição while
#python 2 =    print('O %s tem %d anos.' % (nome,idade))


nome ='jose'
idade = '30'
n = s = 0
while True :
    n = int(input('Digite um numero :  '))
    if n ==999:
        break
    s +=n
# usando f string atualizacao python 3.6
print(f'A soma vale {s}')            
print(f' O {nome} tem {idade} anos')
print(f' O {nome:^20} tem {idade} anos')
print(f' O {nome:-^20} tem {idade} anos') #alinhar no centro
print(f' O {nome:>20} tem {idade} anos')   #alinhar a direita
print(f' O {nome:<20} tem {idade} anos')    #alinhar a esquerda
