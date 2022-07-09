#desafio 85
#ler sete valores
#cadastrar em uma unica lista que mantem sparados pares e impares
#no final motrar todos os valores em ordem crescente

num = [ [] , [] ]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}° valor :'))
    if valor % 2 == 0:
        num[0].append(valor)
    else :
        num[1].append(valor)

num[0].sort()
num[1].sort()

print('===='*10)
print(f'Os valores pares digitados foram  : {num[0]} ')
print(f'Os valores impares digitados foram  :{num[1]}')
