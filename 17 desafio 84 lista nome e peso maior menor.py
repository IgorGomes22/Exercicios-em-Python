#desafio 84
#colocar nome e peso dentro da lista
#quantidade de pessoas cadastradas
#pessoa mais pesadas e mais leves

lista = list()
auxlista = list()

totmaior = 0
totmenor = 0

while True :
    continuar =' '
    auxlista.append(str(input('Seu nome: ')))
    auxlista.append(float(input('Seu peso  : ')))
    if len(lista) == 0 :
             totmaior = auxlista[1]
             totmenor = auxlista[1]
    else:
        if auxlista[1] > totmaior :
             totmaior = auxlista[1]
        if auxlista[1] < totmenor :
             totmenor = auxlista[1]
             
    lista.append(auxlista[:])
    auxlista.clear()
    while continuar not in 'SN' :
        continuar= str(input('Deseja continuar?  [S / N ]')).strip().upper()
    if continuar in 'Nn' :
        break
print('===='*10)
print(f'ao todo foram cadastradas {len(lista)} pessoas !')
print(f'O maior peso é {totmaior} Kg. Peso de :',end=' ')
for p in lista:
    if p[1] == totmaior : 
        print(f' [{p[0]}]',end=' ')
print()

print(f'O menor peso é : {totmenor} Kg. Peso de :',end=' ')
for p in lista:
    if p[1] == totmenor :
        print(f'[{p[0]}]',end=' ')
