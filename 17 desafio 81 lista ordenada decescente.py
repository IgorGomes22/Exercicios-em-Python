#desafio 081
#ler varios numeros colocar em uma lista
#qts num foi digitado
#ordenada decrescente
#valor 5 foi digitado esta na lista sim ou nao


lista= []
c = 0
escolha = ' '

print('****' *10)
while True:
    escolha = ' '
    lista.append(int(input('Digite um valor : ')))
    c += 1
    while escolha not in 'SN' :
        escolha = str(input('Deseja continuar ? [S / N] ')).strip().upper()[0]
    if escolha in 'Nn' :
        break 
print('---'*10)
if 5 in lista:
    print('O numero 5 esta na lista')
else: print('O numero 5 não esta na lista')
print(f'Foi digitado  {c} numeros  ')
lista.sort(reverse=True)
print(lista)
print('****' *10)
