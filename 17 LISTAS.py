# 17 listas
lanche = ['pastel','refri','coxinha','suco','churrasco']
print('=='*10)
for n in lanche:
       print(n)

print('---'*10)
print('comando adicionar item no final da lista')
lanche.append('cafe')
print(lanche)

print('---'*10)

print('adicionar em uma posicao')
lanche .insert(0,'macarrao')
print(lanche)

print('---'*10)

print('deletar item da lista')
del lanche[3]
print(lanche)

print('---'*10)

print('remover item pelo nome/valor')
lanche.remove('suco')
print(lanche)

print('---'*10)

print('remover o ultimo elemento ')
lanche.pop()
print(lanche)

print('---'*10)
 
print('remover item se tiver na lista,verificacao')
if 'pastel' in lanche:
    lanche.remove('pastel')
    print(lanche)

print('---'*10)

print(' colocar numero em ordem crescente')
num = [5,6,8,2,7,3,4,1]
num.sort()
print(num)

print('---'*10)

print('colocar numero em ordem decrescente')
num.sort(reverse=True)
print(num)

print('---'*10)

print(f'Essa lista tem {len(num)} numeros')

print('---'*10)

valores = list()
for cont in range(0,5):
       valores.append(int(input('Digite um valor : ')))

for c,v in enumerate(valores):
       print(f' Na posicao {c} encontrei o valor {v}! ')
print('cheguei ao final da lista')

