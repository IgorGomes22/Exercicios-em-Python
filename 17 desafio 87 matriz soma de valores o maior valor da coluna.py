#desafio 87
#aprimorar o desafio anterior
#a soma de todos os valores pares
#a soma dos valores da terceira coluna
#o maior valor da segunda linha

matriz = [ [0,0,0] , [0,0,0] , [0,0,0] ]
soma = 0
maior = 0
scol = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l] [c] = int(input(f'Digite um valor para [{l}] ,[{c}]'))
       
print('====='*10)

for l in range(0,3):
    for c in range(0,3):
        print(f' [{matriz [l] [c]:^5}]', end=' ')
        if matriz[l][c] %2 == 0 :
            soma += matriz[l][c]
            
    print()

print(f'A soma dos valores pares da matriz é :{soma}')

for l in range(0,3):
    scol += matriz[l][2]
print(f'A soma dos valores da 3° coluna é : {scol} ')

for c in range(0,3):
    if c == 0 :
        maior = matriz[1][c]
    elif matriz[1][c] >maior:
        maior = matriz[1][c]
print(f'O maior valor da 2° linha é : {maior}')
