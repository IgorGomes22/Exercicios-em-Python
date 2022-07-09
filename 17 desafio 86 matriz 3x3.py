#desafio 86
#criar uma matriz de dimensao 3x3
#preencher com valores digitados

matriz = [ [0,0,0] , [0,0,0] , [0,0,0] ]

for l in range(0,3):
    for c in range(0,3) :
        matriz[l] [c] = int(input(f'Digite um valor para [{l}] , [{c}] : '))

print('===='*10)

for l in range(0,3):
    for c in range(0,3):
        print(f' [{matriz[l] [c]}]' , end=' ')
    print()
print(f' A soma dos numeros pares da matriz é : {soma}')
