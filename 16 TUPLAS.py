# aula 16
# TUPLAS

lanche  =(  ' hamburguer ','suco' ,'pizza', 'pudim','batata frita')
print(' lanche == ')
print(lanche)
print('---'*10)
print('lanche [1] ==')
print(lanche [1])
print('---'*10)
print('lanche [-1] == ')
print(lanche [-1])
print('---'*10)
print('lanche [1:3] == ')
print(lanche [1:3])
print('---'*10)
print('lanche [2:] ==')
print(lanche [2:])
print('---'*10)
print('lanche[:2] == ' )
print(lanche [:2])
print('---'*10)

for comida in lanche:
    print(f' Eu vou comer  {comida} ')
    print('---'*10)
print('Eu comi muito ')
print('---'*10)
print('tamanho da lista ==')
print(len(lanche))
print('---'*10)
print('usando laco for com range ')
for cont in range(0,len(lanche)) :
    print(lanche[cont])
    print(f'{cont}  Eu comi {lanche[cont]} ')
print('---'*10)
print('sorted(lanche')
print(sorted(lanche))
print('---'*10)
a = (2,9,4)
b = (1,4,0,6,3)
c = a + b
print(c)
print(c.index(9))   #posicao do elemento
print(c.count(4))  #quantas vezes o elemento 
pessoa = ('Igor', 30 ,'M', 90.00)
print(pessoa)
