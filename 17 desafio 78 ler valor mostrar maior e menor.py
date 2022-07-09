#desafio 78
#ler 5 valores numericos e guardar em uma lista
#moostrar o maior  e menor e suas posicoes

print('---'*10)

num=[]
maior=0
menor=0

for p in range (0,5):
    num.append(int(input(f'Digite o  valor para a posicao {p}:')))
    if p == 0 :
        maior =  menor = num[p]
    else :
        if num[p] > maior :
            maior = num[p]
        if num[p] < menor :
            menor = num[p]
    
print(f'Voce digitou os valores {num}')

print(f'O maior valor digitado foi {max(num)} na posicao   ',end='')
for i,v in enumerate(num):
    if v == maior:
        print(f'{i}...',end='')
print()
print(f'O menor valor digitado foi {min(num)} na posicao   ', end='')
for i,v in enumerate(num):
    if v == menor:
        print(f'{i}...',end='')
print()

print('---'*10)
